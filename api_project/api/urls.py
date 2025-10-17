from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookList, BookViewSet

# Create router instance
router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    # Route for simple ListAPIView
    path('books/', BookList.as_view(), name='book-list'),

    # Routes generated automatically by the router (CRUD)
    path('', include(router.urls)),
]
