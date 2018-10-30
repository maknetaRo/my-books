from django.shortcuts import render, redirect
from django.views.generic import DetailView, ListView, TemplateView
from .forms import BookForm
from django.core.paginator import Paginator

from .models import Book, Author, Genre, Author

class BookDetailView(DetailView):
    model = Book

class AuthorDetailView(DetailView):
    model = Author

class BookListView(ListView):
    template_name = 'books/book_list.html'
    queryset = Book.objects.all()
    context_object_name = 'books'
    paginate_by = 2

class AuthorListView(ListView):
    model = Author 
    paginate_by = 2

class AboutPageView(TemplateView):
    template_name = "books/about.html"

def book_new(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            book.save()
            return redirect('book_detail', pk=book.pk)
    else:
        form = BookForm()
    return render(request, 'books/book_edit.html', {'form': form})

def add_comment_to_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
