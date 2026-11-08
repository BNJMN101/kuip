from django.db.models import Count

from .models import Post


def app_shell(request):
    user = getattr(request, "user", None)
    if not user or not user.is_authenticated:
        return {}

    counts = dict(
        Post.objects.filter(is_active=True)
        .order_by()
        .values_list("category")
        .annotate(n=Count("id"))
    )
    topics = [
        {"value": value, "label": label, "count": counts.get(value, 0)}
        for value, label in Post.Category.choices
    ]
    return {"topics": topics}