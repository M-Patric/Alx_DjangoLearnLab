from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(username, email, password, **extra_fields)


class CustomUser(AbstractUser):
    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(upload_to='profile_photos/', blank=True, null=True)

    objects = CustomUserManager()

    def __str__(self):
        return self.username
class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    publication_year = models.IntegerField()
    profile_photo = models.ImageField(upload_to="profile_photos/", null=True, blank=True)


    class Meta:
        # Define your custom permissions here
        permissions = [
            ("can_create", "Can create book"),
            ("can_delete", "Can delete book"),
            ("can_edit", "Can edit book"),
            ("can_view", "Can view book"),
        ]

    def __str__(self):
        return self.title
# bookshelf/models.py (or where profile_photo lives)
from django.core.exceptions import ValidationError

def validate_image(file):
    limit_mb = 5
    if file.size > limit_mb * 1024 * 1024:
        raise ValidationError("Image too large ( > %sMB )" % limit_mb)
