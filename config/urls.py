from django.contrib import admin
from django.urls import include, path
from discover import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("accounts.urls")),
    path("", views.welcome, name="home"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("post/new/", views.create_post, name="create_post"),
    path("post/<int:pk>/", views.post_detail, name="post_detail"),
    path("post/<int:pk>/edit/", views.edit_post, name="edit_post"),
    path("post/<int:pk>/delete/", views.delete_post, name="delete_post"),
]