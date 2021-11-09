from django.shortcuts import render, redirect, get_object_or_404
from .models import Book

# Create your views here.
def home(request):
    books = Book.objects.all()
    return render(request, "books/home.html",
                  {"books": books})