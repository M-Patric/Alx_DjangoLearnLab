from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("list_books")
    else:
        form = UserCreationForm()
    return render(request, "relationship_app/register.html", {"form": form})
# Helper functions to check user roles
def is_admin(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

def is_librarian(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'

def is_member(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Member'


# Views restricted to each role
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')


@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')


@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')

# helper factory that returns a decorator:
def role_required(role):
    """
    Returns a decorator that allows only users with userprofile.role == role.
    Redirects to LOGIN_URL (name 'login') if not allowed/not logged in.
    """
    def check(user):
        # Must be authenticated and have a userprofile with the required role
        return user.is_authenticated and hasattr(user, "userprofile") and user.userprofile.role == role
    return user_passes_test(check, login_url="login")

# Admin-only view
@role_required("Admin")
def admin_view(request):
    return render(request, "relationship_app/admin_view.html", {"user": request.user})

# Librarian-only view
@role_required("Librarian")
def librarian_view(request):
    return render(request, "relationship_app/librarian_view.html", {"user": request.user})

# Member-only view
@role_required("Member")
def member_view(request):
    return render(request, "relationship_app/member_view.html", {"user": request.user})

# relationship_app/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import permission_required
# from .forms import BookForm  # we'll create this below if missing

# View: list all books
def list_books(request):
    books = Book.objects.all()
    return render(request, "relationship_app/list_books.html", {"books": books})

# Add book — only for users with 'can_add_book'
@permission_required('relationship_app.can_add_book', raise_exception=True)
def add_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("list_books")
    else:
        form = BookForm()
    return render(request, "relationship_app/add_book.html", {"form": form})

# Edit book — only for users with 'can_change_book'
@permission_required('relationship_app.can_change_book', raise_exception=True)
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect("list_books")
    else:
        form = BookForm(instance=book)
    return render(request, "relationship_app/edit_book.html", {"form": form, "book": book})

# Delete book — only for users with 'can_delete_book'
@permission_required('relationship_app.can_delete_book', raise_exception=True)
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == "POST":
        book.delete()
        return redirect("list_books")
    return render(request, "relationship_app/delete_book.html", {"book": book})
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, redirect
from .models import Book

@permission_required('relationship_app.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})


@permission_required('relationship_app.can_create', raise_exception=True)
def add_book(request):
    # Example: Form handling code here
    return render(request, 'add_book.html')


@permission_required('relationship_app.can_edit', raise_exception=True)
def edit_book(request, pk):
    # Example: Logic to edit a book here
    return render(request, 'edit_book.html')


@permission_required('relationship_app.can_delete', raise_exception=True)
def delete_book(request, pk):
    # Example: Logic to delete a book here
    return redirect('book_list')
