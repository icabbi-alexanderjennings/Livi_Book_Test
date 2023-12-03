from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

class Author(models.Model):
    """ The details for an author """
    name = models.CharField(max_length=200, default='', unique=True)

    def __str__(self):
        """ String representation of the model """
        return self.name

class Book(models.Model):
    """ The details for a book """
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, default=0)
    date_published = models.DateField()
    isbn = models.CharField(
        max_length=20,
        default="",
        validators=[
            RegexValidator(
                regex=r'^(?=(?:\D*\d){10}(?:(?:\D*\d){3})?$)[\d-]+$',
                message="Please enter a valid ISDN"
            ),
        ],
    )
    description = models.TextField(default="")

    def __str__(self):
        """ String representation of the model """
        return self.title

class Reading_List(models.Model):
    """ The items in a users reading list """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """ String representation of the model """
        return self.owner + " " +self.book