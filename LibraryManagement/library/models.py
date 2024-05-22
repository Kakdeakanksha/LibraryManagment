# library/models.py

from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    isbn = models.CharField(max_length=13)
    publication_date = models.DateField()
    availability_status = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class Borrower(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    borrowed_books = models.ManyToManyField(Book)

    def __str__(self):
        return self.name

