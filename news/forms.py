from django import forms
from django.core.exceptions import ValidationError

from .models import Post


class PostForm(forms.ModelForm):
    text = forms.CharField(min_length=10)

    class Meta:
        model = Post
        fields = [
            'title',
            'text',
            'author',
            'category',
        ]
