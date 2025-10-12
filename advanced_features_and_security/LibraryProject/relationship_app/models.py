from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    publication_year = models.IntegerField()

    class Meta:
        permissions = [
            ("can_view", "Can view book"),
            ("can_create", "Can create book"),
            ("can_edit", "Can edit book"),
            ("can_delete", "Can delete book"),
        ]

    def __str__(self):
        return self.title
"""
Permission and Group Setup:
- Custom permissions defined in Book.Meta
- Groups (Viewers, Editors, Admins) created via management command
- Views protected with @permission_required decorator
"""
