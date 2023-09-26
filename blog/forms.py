from django import forms
from .models import Post, Category,Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','category', 'content']

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'desc']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)

