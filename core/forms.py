from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):  # Inherits from ModelForm
    class Meta:                   # Meta class defines form metadata
        model = Post             # Specifies which model to base the form on
        fields = ['title', 'content']  # Specifies which fields to include


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Write your comment here...'}),
                   }