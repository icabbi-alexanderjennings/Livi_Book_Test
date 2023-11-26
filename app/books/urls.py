""" URL patterns for the books app """

from django.urls import path
from . import views


app_name = 'books'
urlpatterns = [
    path('', views.index, name='index'),
    # Manage Authors
    path('authors', views.author_list, name='authors'),
    path('author/<int:author_id>/', views.author_single, name='author'),
    path('author_add', views.author_add, name='author_add'),
    path('author_edit/<int:author_id>/', views.author_edit, name='author_edit'),
    path('author_delete/<int:author_id>/', views.author_delete, name='author_delete'),
    # Manage Books
    path('books', views.book_list, name='books'),
    path('book_add', views.book_add, name='book_add'),
    path('book_edit/<int:book_id>/', views.book_edit, name='book_edit'),
    path('book_delete/<int:book_id>/', views.book_delete, name='book_delete'),
    # Manage Reading List
    path('reading_list', views.reading_list, name='reading_list'),
    path('reading_list_add/<int:book_id>/', views.reading_list_add, name='reading_list_add'),
    path('reading_list_delete/<int:book_id>/', views.reading_list_delete, name='reading_list_delete'),
]