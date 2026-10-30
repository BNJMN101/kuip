from django.conf import settings
from django.db import models
from django.utils import timezone

class Post(models.Model):
    class Category(models.TextChoices):
        OPPORTUNITY = "opportunity", "Opportunities"
        DISCOVER = "discover", "Discover"
        REQUEST = "request", "Requests"

    title = models.CharField(max_length=140)
    category = models.CharField(max_length=20, choices=Category.choices)
    description = models.TextField(max_length=3000)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        related_name="posts",
        null=True,
        blank=True,
    )
    link = models.URLField(blank=True, help_text="Official source, useful link, or contact page (optional).")
    deadline = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title

    @property
    def is_expired(self):
        return self.deadline is not None and self.deadline < timezone.localdate()


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        related_name="comments",
        null=True,
        blank=True,
    )
    body = models.TextField(max_length=1000)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ["created_at"]

    def __str__(self):
        return f"Comment by {self.author} on {self.post}"