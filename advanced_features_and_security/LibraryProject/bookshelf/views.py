from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from .models import Book

# 👇 The view required by the checker
@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    # Retrieve all books from the database
    books = Book.objects.all()
    # Render the books list template
    return render(request, 'bookshelf/book_list.html', {'books': books})
