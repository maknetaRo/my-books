from django.urls import path
from books.views import AboutPageView, BookListView, BookDetailView, AuthorListView, AuthorDetailView, TitleListView
from . import views

urlpatterns = [

    path('', BookListView.as_view(), name='books'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('book/<int:pk>/', BookDetailView.as_view(), name='book_detail'),
    path('book/new/', views.book_new, name='book_new'),
    path('book/<int:pk>/edit/', views.book_edit, name='book_edit'),
    path('titles/', TitleListView.as_view(), name='titles'),
    path('authors/', AuthorListView.as_view(), name='authors'),
    path('author/<int:pk>/', AuthorDetailView.as_view(), name='author_detail'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('register', views.register_user, name='register'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('change_password/', views.change_password, name='change_password'),
]
