from django.contrib import admin
from books.models import Genre, Book, Author, Comment, Language


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name',
                    'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]


admin.site.register(Author, AuthorAdmin)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre', 'display_language', 'stars')


admin.site.register(Genre)
admin.site.register(Language)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'book', 'created', 'approved_comment')
    list_filter = ('approved_comment', 'created')
    search_fields = ('name', 'email', 'body')
