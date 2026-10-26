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
    author_name = models.CharField(max_length=80, default="Community member")
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
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
