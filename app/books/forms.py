from django.forms import ModelForm, DateInput, TextInput
from .models import Author, Book

class DateInput(DateInput):
    input_type = 'date'

class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = ['name']
        labels = {
            'name': 'Name',
        }

class BookForm(ModelForm):
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
            'date_published': DateInput(),
        }