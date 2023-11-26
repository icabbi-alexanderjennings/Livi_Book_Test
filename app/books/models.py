from django.db import models
from django.contrib.auth.models import User

class Author(models.Model):
    """ The details for an author """
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        """ String representation of the model """
        return self.first_name + " " +self.last_name

class Book(models.Model):
    """ The details for a book """
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, default=0)
    date_published = models.DateTimeField()
    isbn = models.CharField(max_length=20, default="")
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