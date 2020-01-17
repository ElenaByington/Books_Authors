from django.shortcuts import render, redirect
from .models import *

# Create your views here.
def index(request):
    all_books = Book.objects.all()
    context = {
        "books":all_books
    }
    return render(request, 'index.html', context)

def add_new_book(request):
    Book.objects.create(title=request.POST['title'], description=request.POST['description'])
    return redirect('/')
    
def book_page(request, id):
    book = Book.objects.get(id=id)
    all_authors = Author.objects.all()
    context = {
        "book":book,
        "authors":all_authors
    }
    return render(request,'book_page.html', context)

def select_author(request, id):
    print (request.POST)
    option = Author.objects.get(id = request.POST['author'])
    Book.objects.get(id=id).authors.add(option)
    return redirect(f'/books/{id}')

def author(request):
    all_authors = Author.objects.all()
    context = {
        "authors":all_authors
    }
    return render(request, 'add_authors.html', context)

def add_new_author(request):
    Author.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], notes=request.POST['notes'])
    return redirect(f'/authors')

def author_page(request, id):
    author = Author.objects.get(id=id)
    all_books = Book.objects.all()
    context = {
        "author":author,
        "books":all_books
    }
    return render(request,'author_page.html', context)

def select_book(request, id):
    print (request.POST)
    option = Book.objects.get(id = request.POST['book'])
    Author.objects.get(id=id).books.add(option)
    return redirect(f'/authors/{id}')
