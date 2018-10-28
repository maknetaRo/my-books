from django.urls import path
from books.views import AboutPageView, BookListView, BookDetailView

urlpatterns = [

        path('', BookListView.as_view(), name='books'),
        path('about/', AboutPageView.as_view(), name='about'),
        path('book/<int:pk>/', BookDetailView.as_view(), name='book_detail')
]
