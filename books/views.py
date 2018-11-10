from django.shortcuts import render, redirect
from django.views.generic import DetailView, ListView, TemplateView
from django.core.paginator import Paginator
from .models import Book, Author, Genre, Author, Comment
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages
from .forms import SignUpForm, EditProfileForm, CommentForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


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
    comments = post.comments.filter(active=True)

    new_comment = None

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
    else:
        comment_form = CommentForm()
    return render(request,
                 'books/book_detail.html',
                 {'post' : post,
                 'comments': comments,
                 'new_comment': new_comment,
                 'comment_form': comment_form})


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

class AuthorCreate(CreateView):
    model = Author
    fields = '__all__'
    initial = {'date_of_death': '07/11/2018'}

class AuthorUpdate(UpdateView):
    model = Author
    fields = ['first_name', 'last_name', 'date_of_birth', 'date_of_death']

class AuthorDelete(DeleteView):
    model = Author
    success_url = reverse_lazy('authors')

class BookCreate(CreateView):
    model = Book
    fields = '__all__'

class BookUpdate(UpdateView):
    model = Book
    fields = ['author', 'title', 'text', 'genre', 'language']

class BookDelete(DeleteView):
    model = Book
    success_url = reverse_lazy('authors')
