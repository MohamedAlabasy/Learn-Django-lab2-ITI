from django.shortcuts import render

# Create your views here.


def list_books(request):
    context = {
        "data": "data"
    }
    return render(request, 'books/list_books.html', context=context)


def show_book(request, book_id):
    context = {
        "data": book_id
    }
    return render(request, 'books/show_book.html', context=context)


def list_authors(request):
    context = {
        "data": "data"
    }
    return render(request, 'books/list_authors.html', context=context)


def show_author(request, author_id):
    context = {
        "data": author_id
    }
    return render(request, 'books/show_author.html', context=context)
