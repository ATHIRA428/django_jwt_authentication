from django.urls import path
from .views import (
    BookListView,
    BookCreateView,
    BookUpdateView,
    BookDeleteView,
    UserRegistrationView,
   
)

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='user-registration'),
    path('books/', BookListView.as_view(), name='book-list'),
    path('books/create/', BookCreateView.as_view(), name='book-create'),
    path('books/<int:pk>/update/', BookUpdateView.as_view(), name='book-update'),
    path('books/<int:pk>/delete/', BookDeleteView.as_view(), name='book-delete'),
]








