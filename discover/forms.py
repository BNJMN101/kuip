from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "category", "description", "author_name", "link", "deadline"]
        widgets = {
            "title": forms.TextInput(attrs={"placeholder": "e.g. Python study group or internship opening"}),
            "description": forms.Textarea(attrs={"rows": 5, "placeholder": "Share the details people need to know..."}),
            "author_name": forms.TextInput(attrs={"placeholder": "Your name or a nickname"}),
            "link": forms.URLInput(attrs={"placeholder": "https://..."}),
            "deadline": forms.DateInput(attrs={"type": "date"}),
        }
        help_texts = {
            "category": "Choose the type that best describes this post.",
            "deadline": "Mainly for time-sensitive opportunities. Leave blank if it doesn't apply.",
        }

    def clean_title(self):
        title = self.cleaned_data["title"].strip()
        if len(title) < 4:
            raise forms.ValidationError("Please use a title with at least 4 characters.")
        return title
