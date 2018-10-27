from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Book, Author, Genre


class BookListView(ListView):
    template_name = 'book_list.html'
    queryset = Book.objects.all()
    context_object_name = 'books'
    paginate_by = 10
