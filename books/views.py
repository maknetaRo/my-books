from django.shortcuts import render, redirect
from django.views.generic import DetailView, ListView, TemplateView
from .forms import BookForm
from django.core.paginator import Paginator
from .models import Book, Author, Genre, Author
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages
from .forms import SignUpForm, EditProfileForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm


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


class AuthorDetailView(DetailView):
    model = Author


class BookListView(ListView):
    template_name = 'books/book_list.html'
    queryset = Book.objects.all()
    context_object_name = 'books'
    paginate_by = 2


class TitleListView(ListView):
    template_name = 'books/title_list.html'
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
