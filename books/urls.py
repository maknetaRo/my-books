from django.urls import path
from books.views import AboutPageView, BookListView, BookDetailView
from . import views

urlpatterns = [

        path('', BookListView.as_view(), name='books'),
        path('about/', AboutPageView.as_view(), name='about'),
        path('book/<int:pk>/', BookDetailView.as_view(), name='book_detail'),
        path('book/new/', views.book_new, name='book_new'),
]
