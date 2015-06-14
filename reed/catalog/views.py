from django.shortcuts import render

from .models import Book


def book_list(request):
    books = Book.objects.all()
    context = {
        'books': books,
    }
    return render(request, 'catalog/index.html', context)

def book_detail(request, book_id):
    book = Book.objects.get(pk=book_id)
    context = {
        'book': book,
    }
    return render(request, 'catalog/book.html', context)
