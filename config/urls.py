from django.contrib import admin
from django.urls import path
from discover import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="home"),
    path("post/new/", views.create_post, name="create_post"),
    path("post/<int:pk>/", views.post_detail, name="post_detail"),
]
