from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Post

User = get_user_model()


class PostOwnershipTests(TestCase):
    def setUp(self):
        self.alice = User.objects.create_user(
            username="alice", email="alice@example.com", password="StrongPass123!"
        )
        self.bob = User.objects.create_user(
            username="bob", email="bob@example.com", password="StrongPass123!"
        )
        self.post = Post.objects.create(
            title="Alice's internship post",
            category=Post.Category.OPPORTUNITY,
            description="Some details.",
            author=self.alice,
        )

    def test_logged_out_visitor_is_sent_to_login(self):
        response = self.client.get(reverse("dashboard"))
        self.assertRedirects(response, f"{reverse('login')}?next={reverse('dashboard')}")

    def test_owner_can_open_edit_page(self):
        self.client.force_login(self.alice)
        response = self.client.get(reverse("edit_post", args=[self.post.pk]))
        self.assertEqual(response.status_code, 200)

    def test_other_user_gets_404_on_edit_page(self):
        self.client.force_login(self.bob)
        response = self.client.get(reverse("edit_post", args=[self.post.pk]))
        self.assertEqual(response.status_code, 404)

    def test_other_user_cannot_delete_post(self):
        self.client.force_login(self.bob)
        response = self.client.post(reverse("delete_post", args=[self.post.pk]))
        self.assertEqual(response.status_code, 404)
        self.assertTrue(Post.objects.filter(pk=self.post.pk).exists())