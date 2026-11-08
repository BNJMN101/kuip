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

class DashboardTests(TestCase):
    def setUp(self):
        self.alice = User.objects.create_user(username="alice", password="StrongPass123!")
        self.bob = User.objects.create_user(username="bob", password="StrongPass123!")
        Post.objects.create(
            title="Post by Alice", category=Post.Category.IDEA,
            description="Hell``o", author=self.alice,
        )
        Post.objects.create(
            title="Post by Bob", category=Post.Category.IDEA,
            description="Hello", author=self.bob,
        )

    def test_dashboard_shows_all_posts(self):
        self.client.force_login(self.alice)
        response = self.client.get(reverse("dashboard"))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context["posts"]), 2)

    def test_my_posts_filter_only_returns_own_posts(self):
        self.client.force_login(self.alice)
        response = self.client.get(reverse("dashboard"), {"mine": "1"})
        titles = [post.title for post in response.context["posts"]]
        self.assertEqual(titles, ["Post by Alice"])

    def test_search_ignores_topic_filter(self):
        Post.objects.create(
            title="Gist about jollof", category=Post.Category.FUN,
            description="Party or smoky?", author=self.bob,
        )
        self.client.force_login(self.alice)
        response = self.client.get(reverse("dashboard"), {"q": "jollof", "category": "idea"})
        titles = [post.title for post in response.context["posts"]]
        self.assertEqual(titles, ["Gist about jollof"])

    def test_search_matches_author_username(self):
        self.client.force_login(self.alice)
        response = self.client.get(reverse("dashboard"), {"q": "bob"})
        titles = [post.title for post in response.context["posts"]]
        self.assertEqual(titles, ["Post by Bob"])

    def test_search_with_no_matches_still_loads(self):
        self.client.force_login(self.alice)
        response = self.client.get(reverse("dashboard"), {"q": "zzzzqqq"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context["posts"]), 0)