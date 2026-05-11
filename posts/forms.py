from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['post_title', 'post_content']
        widgets = {
            'post_title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter post title'}),
            'post_content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter post content', 'rows': 5}),
        }
