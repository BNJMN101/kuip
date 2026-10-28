from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "author", "created_at", "deadline", "is_active")
    list_filter = ("category", "is_active")
    search_fields = ("title", "description", "author")
    list_editable = ("is_active",)
