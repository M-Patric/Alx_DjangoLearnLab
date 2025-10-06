from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import models
class UserProfile(models.Model):
    ROLE_ADMIN = "Admin"
    ROLE_LIBRARIAN = "Librarian"
    ROLE_MEMBER = "Member"

    ROLE_CHOICES = [
        (ROLE_ADMIN, "Admin"),
        (ROLE_LIBRARIAN, "Librarian"),
        (ROLE_MEMBER, "Member"),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="userprofile")
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default=ROLE_MEMBER)

    def __str__(self):
        return f"{self.user.username} ({self.role})"


# Create UserProfile automatically when a new User is created
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

# Ensure profile exists on each save (defensive)
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    publication_year = models.PositiveIntegerField()

    def __str__(self):
        return self.title

    class Meta:
        permissions = [
            ("can_add_book", "Can add book"),
            ("can_change_book", "Can change book"),
            ("can_delete_book", "Can delete book"),
        ]