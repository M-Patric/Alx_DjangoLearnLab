from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from relationship_app.models import Book

class Command(BaseCommand):
    help = 'Sets up default groups and assigns permissions'

    def handle(self, *args, **kwargs):
        # Define groups
        groups_permissions = {
            "Viewers": ["can_view"],
            "Editors": ["can_view", "can_create", "can_edit"],
            "Admins": ["can_view", "can_create", "can_edit", "can_delete"],
        }

        for group_name, perms in groups_permissions.items():
            group, created = Group.objects.get_or_create(name=group_name)
            for perm_code in perms:
                try:
                    permission = Permission.objects.get(codename=perm_code, content_type__app_label="relationship_app")
                    group.permissions.add(permission)
                except Permission.DoesNotExist:
                    self.stdout.write(self.style.ERROR(f"Permission {perm_code} not found."))
            self.stdout.write(self.style.SUCCESS(f"{group_name} group updated."))
