from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import DetailView, ListView, TemplateView
from django.core.paginator import Paginator
from .models import Book, Author, Genre, Author, Comment, Quote
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages
from .forms import SignUpForm, EditProfileForm, CommentForm, QuoteForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'books/book_list.html', {})


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ("You Have Been Login!"))
            return redirect('books')
        else:
            messages.success(request, ('Error Logging - Please Try Again...'))
            return redirect('login')
    else:
        return render(request, 'books/registration/login.html', {})


def user_logout(request):
    logout(request)
    messages.success(request, ("You Have Been Logged Out..."))
    return redirect('books')


def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)
            login(request, user)
            messages.success(request, ('You Have Registered...'))
            return redirect('books')
    else:
        form = SignUpForm()
    context = {'form': form}
    return render(request, 'books/registration/register.html', context)


def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()

            messages.success(request, ('You Have Edited Your Profile ...'))
            return redirect('books')
    else:
        form = EditProfileForm(instance=request.user)
    context = {'form': form}
    return render(request, 'books/registration/edit_profile.html', context)


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, ('You Have Edited your Password ...'))
            return redirect('books')

    else:
        form = PasswordChangeForm(user=request.user)
    context = {'form': form}
    return render(request, 'books/registration/change_password.html', context)

class BookDetailView(DetailView):
    model = Book

def add_comment_to_book(request, pk):
    book = get_object_or_404(Book, pk=pk)

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.book = book
            comment.save()
            return redirect('book_detail', pk=book.pk)
    else:
        form = CommentForm()
    return render(request,
                 'books/add_comment_to_book.html',
                 {'form':form})

@login_required
def comment_approve(requeste, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('book_detail', pk=comment.book.pk)

@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.delete()
    return redirect('book_detail', pk=comment.book.pk)

@login_required
def add_quote_to_book(request, pk):
    book = get_object_or_404(Book, pk=pk)

    if request.method == "POST":
        form = QuoteForm(request.POST)
        if form.is_valid():
            quote = form.save(commit=False)
            quote.book = book
            quote.save()
            return redirect('book_detail', pk=book.pk)
    else:
        form = QuoteForm()
    return render(request,
                 'books/add_quote_to_book.html',
                 {'form':form})


class AuthorDetailView(DetailView):
    model = Author


class BookListView(ListView):
    template_name = 'books/book_list.html'
    queryset = Book.objects.all()
    context_object_name = 'books'
    paginate_by = 5


class TitleListView(ListView):
    template_name = 'books/title_list.html'
    queryset = Book.objects.all()
    context_object_name = 'books'
    paginate_by = 20


class AuthorListView(ListView):
    template_name = "books/author_list.html"
    model = Author
    paginate_by = 20


class AboutPageView(TemplateView):
    template_name = "books/about.html"

class AuthorCreate(CreateView):
    model = Author
    fields = '__all__'
    template_name = 'books/author_create.html'


class AuthorUpdate(UpdateView):
    model = Author
    fields = ['first_name', 'last_name', 'date_of_birth', 'date_of_death', 'description', 'image']
    template_name = 'books/author_update.html'

class AuthorDelete(DeleteView):
    model = Author
    success_url = reverse_lazy('authors')

class BookCreate(CreateView):
    model = Book
    fields = '__all__'
    template_name = 'books/book_new.html'

class BookUpdate(UpdateView):
    model = Book
    fields = ['author', 'title', 'text', 'genre', 'language', 'image']
    template_name = 'books/book_edit.html'

class BookDelete(DeleteView):
    model = Book
    success_url = reverse_lazy('books')

class GenreListView(ListView):
    template_name = 'books/list_genre.html'
    model = Genre
