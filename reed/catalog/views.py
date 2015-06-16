from django.shortcuts import render

from rest_framework import viewsets

from .models import Book
from . import forms
from . import serializers


def book_list(request):
    books = Book.objects.all()
    context = {
        'books': books,
    }
    return render(request, 'catalog/book_list.html', context)

def book_detail(request, book_id):
    book = Book.objects.get(pk=book_id)
    context = {
        'book': book,
    }
    return render(request, 'catalog/book_detail.html', context)

def intro_python(request):
    books = Book.objects.python_book().intro_book()
    context = {
        'books': books,
    }
    return render(request, 'catalog/book_list.html', context)


def search(request):
    context = {}
    if 'query' in request.GET:
        form = forms.SearchForm(request.GET)
        context['form'] = form
        if form.is_valid():
            context['books'] = Book.objects.filter(title__icontains=form.cleaned_data['query'])
        else:
            context['books'] = Book.objects.none()
    else:
        context['form'] = forms.SearchForm()
        context['books'] = Book.objects.none()
    return render(request, 'catalog/book_search.html', context)

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = serializers.BookSerializer

