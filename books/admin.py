from django.contrib import admin
from books.models import Genre, Book, Author

admin.site.register(Genre)
admin.site.register(Book)
admin.site.register(Author)
