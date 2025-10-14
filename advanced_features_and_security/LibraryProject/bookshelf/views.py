from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from .models import Book

@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    # Retrieve all books from the database
    books = Book.objects.all()
    # Render the books list template
    return render(request, 'bookshelf/book_list.html', {'books': books})

from django.shortcuts import render
from .models import Book
from .forms import BookSearchForm
from django.db.models import Q

def book_search(request):
    form = BookSearchForm(request.GET or None)
    books = Book.objects.none()
    if form.is_valid():
        q = form.cleaned_data.get("q")
        # Use ORM filters, parameterized safely by Django
        if q:
            books = Book.objects.filter(Q(title__icontains=q) | Q(author__icontains=q))
        else:
            books = Book.objects.all()
    return render(request, "bookshelf/book_list.html", {"form": form, "books": books})
