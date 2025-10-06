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