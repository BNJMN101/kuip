from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("communities/", views.communities, name="communities"),
    path("how-it-works/", views.how_it_works, name="how_it_works"),
    path("about/", views.about, name="about"),
    path("guidelines/", views.guidelines, name="guidelines"),
]