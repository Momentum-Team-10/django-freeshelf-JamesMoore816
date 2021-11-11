from django.shortcuts import render, redirect, get_object_or_404
from .models import Book, Category
from .forms import BookForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    books = reversed(Book.objects.all())
    categories = (Category.objects.all())
    return render(request, "books/home.html",
                  {"books": books, "categories": categories,})

def view_book(request, slug):
    book = get_object_or_404(Book, slug=slug)
    return render(request, "books/view_book.html",
                  {"book": book})

@login_required
def add_book(request):
    if request.method == 'GET':
        form = BookForm()
    else:
        form = BookForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='home')

    return render(request, "books/add_book.html", {"form": form})

@login_required
def edit_book(request, slug):
    book = get_object_or_404(Book, slug=slug)
    if request.method == 'GET':
        form = BookForm(instance=book)
    else:
        form = BookForm(data=request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect(to='/')

    return render(request, "books/edit_book.html", {
        "form": form,
        "book": book
    })

@login_required
def delete_book(request, slug):
    book = get_object_or_404(Book, slug=slug)
    if request.method == 'POST':
        book.delete()
        return redirect(to='/')

    return render(request, "books/delete_book.html",
                  {"book": book})

def category_search(request, slug):
    category = get_object_or_404(Category, slug=slug)
    books = reversed(Book.objects.filter(categories__slug=slug))
    return render(request, "books/category_search.html",
                  {"books": books, "category": category,})

@login_required
def profile(request):
    user = request.user
    books = reversed(Book.objects.filter(favorite=user.pk))
    categories = (Category.objects.all())
    return render(request, "books/profile.html",
                  {"user": user, "books": books, "categories": categories,})