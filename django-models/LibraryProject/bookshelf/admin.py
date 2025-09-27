from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # Columns shown on the list (change list view)
    list_display = ("id", "title", "author", "publication_year")

    # Make the title column clickable (link to change view)
    list_display_links = ("title",)

    # Which fields are editable directly from the list page
    # NOTE: fields in list_editable cannot appear in list_display_links
    list_editable = ("author", "publication_year")

    # Filter sidebar (quick filtering)
    list_filter = ("author", "publication_year")

    # Search box (search title and author). Prefix '^' for startswith.
    search_fields = ("^title", "author")

    # Default ordering in list view
    ordering = ("-publication_year", "title")

    # How many items per list page
    list_per_page = 25

    # Make some fields read-only in the change form (if any)
    # readonly_fields = ("id",)  # uncomment if you want ID readonly

    # Optional: group fields in the edit form
    # fieldsets = (
    #     (None, {"fields": ("title", "author")}),
    #     ("Publication Info", {"fields": ("publication_year",)}),
    # )
