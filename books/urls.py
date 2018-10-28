from django.urls import path
from books.views import AboutPageView, BookListView

urlpatterns = [

        path('', BookListView.as_view(), name='books'),
        path('about/', AboutPageView.as_view(), name='about'),
]
