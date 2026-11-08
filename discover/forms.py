from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "category", "description", "link"]
        widgets = {
            "title": forms.TextInput(attrs={"placeholder": "An interesting title"}),
            "description": forms.Textarea(attrs={"rows": 6, "placeholder": "Write what you want to share..."}),
            "link": forms.URLInput(attrs={"placeholder": "https://..."}),
        }
        help_texts = {
            "category": "Pick the topic that fits best.",
        }

    def clean_title(self):
        title = self.cleaned_data["title"].strip()
        if len(title) < 4:
            raise forms.ValidationError("Please use a title with at least 4 characters.")
        return title