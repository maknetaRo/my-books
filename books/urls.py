from django.urls import path
from books.views import AboutPageView, BookListView, BookDetailView, AuthorListView, AuthorDetailView, TitleListView
from books.views import BookCreate, BookUpdate, BookDelete, AuthorCreate, AuthorUpdate, AuthorDelete
from . import views

urlpatterns = [

    path('', BookListView.as_view(), name='books'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('book/<int:pk>/', BookDetailView.as_view(), name='book_detail'),
    path('book/new/', BookCreate.as_view(), name='book_new'),
    path('book/<int:pk>/edit/', BookUpdate.as_view(), name='book_edit'),
    path('book/<int:pk>/delete/', BookDelete.as_view(), name='book_delete'),
    path('titles/', TitleListView.as_view(), name='titles'),
    path('authors/', AuthorListView.as_view(), name='authors'),
    path('author/<int:pk>/', AuthorDetailView.as_view(), name='author_detail'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('register', views.register_user, name='register'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('change_password/', views.change_password, name='change_password'),
    path('author/create/', views.AuthorCreate.as_view(), name='author_create'),
    path('author/<int:pk>/update/', views.AuthorUpdate.as_view(), name='author_update'),
    path('author/<int:pk>/delete/', views.AuthorDelete.as_view(), name='author_delete'),
]
