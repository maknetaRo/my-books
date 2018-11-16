from django.db import models
from django.urls import reverse
from django.utils import timezone


class Genre(models.Model):
    name = models.CharField(max_length=200, help_text='Enter a book genre')

    def __str__(self):
        return self.name

class Language(models.Model):
    name = models.CharField(max_length=200, help_text='Podaj język w jakim napisana jest książka')

    def __str__(self):
        return self.name


class Book(models.Model):
    author = models.ForeignKey('Author', on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=200)
    text = models.TextField(max_length=50000)
    genre = models.ManyToManyField('Genre', help_text='Select a genre for a book')
    language = models.ManyToManyField('Language')
    image = models.ImageField(upload_to='static/img/books', blank=True)


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book_detail', args=[str(self.id)])

    def display_genre(self):
        return ', '.join(genre.name for genre in self.genre.all()[:3])

    display_genre.short_description = 'Gatunek'

    def display_language(self):
        return ', '.join(language.name for language in self.language.all()[:3])

    display_language.short_description = 'Język'

    def approved_comments(self):
        return self.comments.filter(approved_comment=True)

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)
    description = models.TextField(max_length=50000, null=True, blank=True)
    image = models.ImageField(upload_to='static/img/authors', blank=True)

    class Meta:
        ordering = ['last_name', 'first_name']

    def get_absolute_url(self):
        return reverse('author_detail', kwargs={'pk' : self.pk})

    def __str__(self):
        return f'{self.last_name}, {self.first_name}'


class Comment(models.Model):
    book = models.ForeignKey('Book', on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField(max_length=5000)
    created = models.DateTimeField(auto_now_add=True)
    approved_comment = models.BooleanField(default=False)

    class Meta:
        ordering = ('created',)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.body
