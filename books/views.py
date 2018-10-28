from django.shortcuts import render
from django.views.generic import DetailView, ListView, TemplateView

from .models import Book, Author, Genre

class BookDetailView(DetailView):
    model = Book

class BookListView(ListView):
    template_name = 'book_list.html'
    queryset = Book.objects.all()
    context_object_name = 'books'
    paginate_by = 10

class AboutPageView(TemplateView):
    template_name = "books/about.html"

def add_comment_to_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
