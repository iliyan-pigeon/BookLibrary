from django.urls import path
from BookLibrary.BookLibraryAPI.views import get_data, add_book

urlpatterns = [
    path('', get_data),
    path('add/', add_book),
]
