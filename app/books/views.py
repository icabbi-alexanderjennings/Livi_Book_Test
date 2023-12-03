from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Author, Book, Reading_List
from .forms import AuthorForm, BookForm

def index(request):
    return render(request, 'books/index.html')

# Code for handling Authors
def author_list(request):
    """ Show all the authors """
    authors = Author.objects.order_by('name')
    context = {'authors': authors}
    return render(request, 'books/authors.html', context)

def author_single(request, author_id):
    """ Show a specific author and all their books """
    author = Author.objects.get(id=author_id)
    books = author.book_set.order_by('date_published')
    context = {'author': author, 'books': books}
    return render(request, 'books/author.html', context)

def author_search(request):
    """ Find Authors """
    if 'search' in request.GET:
        authors = Author.objects.all().filter(name__contains=request.GET['search']).order_by('name')
    else:
        authors = Author.objects.order_by('name')
    context = {'authors': authors}
    return render(request, 'books/authors.html', context)

@login_required
def author_add(request):
    """ Add a new author to the database """
    if request.method != 'POST':
        form = AuthorForm()
    else:
        form = AuthorForm(data=request.POST)
        if form.is_valid():
            form.save()
            if "author_add" in request.META['HTTP_REFERER']:
                return redirect('books:authors')
            else:
                return redirect(request.META['HTTP_REFERER'])

    context = {'form': form}
    return render(request, 'books/author_add.html', context)

@login_required
def author_edit(request, author_id):
    """ Edit an existing author """
    author = Author.objects.get(id=author_id)

    if request.method != 'POST':
        form = AuthorForm(instance=author)
    else:
        form = AuthorForm(instance=author, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('books:authors')

    context = {'form': form, 'author': author}
    return render(request, 'books/author_edit.html', context)

@login_required
def author_delete(request, author_id):
    """ Delete an author from the database """
    Author.objects.get(id=author_id).delete()

    return redirect('books:authors')

# Code for handling Books
def book_list(request):
    """ Show all the books """
    books = Book.objects.order_by('title')
    context = {'books': books}
    return render(request, 'books/books.html', context)

def book_search(request):
    """ Find books """
    if 'search' in request.GET:
        books = Book.objects.all().filter(title__contains=request.GET['search']).order_by('title')
    else:
        books = Book.objects.order_by('title')
    context = {'books': books}
    return render(request, 'books/books.html', context)

@login_required
def book_add(request):
    """ Add a new book to the database """
    author_form = AuthorForm()
    if request.method != 'POST':
        book_form = BookForm()
    else: 
        book_form = BookForm(data=request.POST)
        if book_form.is_valid():
            book_form.save()
            return redirect('books:books')

    context = {'author_form': author_form, 'book_form': book_form}
    return render(request, 'books/book_add.html', context)

@login_required
def book_edit(request, book_id):
    """ Edit an existing book """
    book = Book.objects.get(id=book_id)

    if request.method != 'POST':
        form = BookForm(instance=book)
    else:
        form = BookForm(instance=book, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('books:books')

    context = {'form': form, 'book': book}
    return render(request, 'books/book_edit.html', context)

@login_required
def book_delete(request, book_id):
    """ Delete an book from the database """
    Book.objects.get(id=book_id).delete()

    return redirect('books:books')

# Code for handling Reading Lists
@login_required
def reading_list(request):
    """ Show the users personal reading list """
    reading_list = Reading_List.objects.filter(owner=request.user).order_by('date_added')
    context = {'reading_list': reading_list}
    return render(request, 'books/reading_list.html', context)

@login_required
def reading_list_search(request):
    """ Find books in reading list """
    if 'search' in request.GET:
        reading_list = Reading_List.objects.filter(owner=request.user).filter(book__title__contains=request.GET['search']).order_by('book__title')
    else:
        reading_list = Reading_List.objects.filter(owner=request.user).order_by('date_added')
    context = {'reading_list': reading_list}
    return render(request, 'books/reading_list.html', context)

@login_required
def reading_list_add(request, book_id):
    """ Add to the users personal reading list """
    book = Book.objects.get(id=book_id)
    if Reading_List.objects.filter(owner=request.user).filter(book=book_id).exists():
        # This item is already in the reading list
        return redirect('books:reading_list')
    else:
        # Add the book
        new_reading = Reading_List(owner=request.user, book=book)
        new_reading.save()
        return redirect('books:reading_list')

@login_required
def reading_list_delete(request, book_id):
    """ Remove from the users personal reading list """
    Reading_List.objects.filter(owner=request.user, book=book_id).delete()
    return redirect('books:reading_list')
