from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from .forms import PostForm
from .models import Post

@login_required
def dashboard(request):
    posts = Post.objects.filter(is_active=True).select_related("author")
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
def edit_post(request, pk):
    post = get_object_or_404(Post, pk=pk, author=request.user)

    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, "Your post was updated.")
            return redirect("post_detail", pk=post.pk)
    else:
        form = PostForm(instance=post)

    return render(request, "discover/create_post.html", {"form": form, "editing": True})

@login_required
def delete_post(request, pk):
    post = get_object_or_404(Post, pk=pk, author=request.user)

    if request.method == "POST":
        post.delete()
        messages.success(request, "Your post was deleted.")
        return redirect("dashboard")

    return render(request, "discover/post_confirm_delete.html", {"post": post})

@login_required
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk, is_active=True)
    return render(request, "discover/post_detail.html", {"post": post})
