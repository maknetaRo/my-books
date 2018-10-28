from .models import Comment, Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('title', 'text')


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')
