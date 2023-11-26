from django import forms
from django.forms import ModelForm
from .models import Author, Book

class DateInput(forms.DateInput):
    input_type = 'date'

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['first_name', 'last_name']
        labels = {
            'first_name': 'First Name: ',
            'last_name': 'Last Name: ',
        }

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'date_published', 'isbn', 'description']
        labels = {
            'title': 'Title',
            'author': 'Author',
            'date_published': 'Published',
            'isbn': 'ISBN',
            'description': 'Description',
        }
        widgets = {
            'date_published': DateInput()
        }