# urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.list_books),
    path('books/create/', views.create_book),
    path('books/<int:pk>/', views.book_detail),
    # Define other URL patterns for Borrower endpoints...
]
