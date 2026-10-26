from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from .forms import PostForm
from .models import Post

@login_required
def dashboard(request):
    posts = Post.objects.filter(is_active=True)
    category = request.GET.get("category", "").strip()
    query = request.GET.get("q", "").strip()

    valid_categories = {choice[0] for choice in Post.Category.choices}
    if category in valid_categories:
        posts = posts.filter(category=category)
    else:
        category = ""

    if query:
        posts = posts.filter(Q(title__icontains=query) | Q(description__icontains=query))

    return render(request, "discover/dashboard.html", {
        "posts": posts,
        "selected_category": category,
        "query": query,
        "categories": Post.Category.choices,
    })

def welcome(request):
    return render(request, "discover/welcome.html")

@login_required
def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            messages.success(request, "Your post is live in the community feed.")
            return redirect("post_detail", pk=post.pk)
    else:
        form = PostForm()
    return render(request, "discover/create_post.html", {"form": form})

@login_required
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk, is_active=True)
    return render(request, "discover/post_detail.html", {"post": post})
