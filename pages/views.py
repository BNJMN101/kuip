from django.shortcuts import render


def home(request):
    return render(request, "pages/home.html")


def communities(request):
    return render(request, "pages/communities.html")


def how_it_works(request):
    return render(request, "pages/how_it_works.html")


def about(request):
    return render(request, "pages/about.html")


def guidelines(request):
    return render(request, "pages/guidelines.html")