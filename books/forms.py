from django import forms 
from .models import Comment, Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('title', 'author', 'text', 'genre')


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')
