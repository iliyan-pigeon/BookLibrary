from django.urls import path
from BookLibrary.BookLibraryAPI.views import get_data, add_book, get_book

urlpatterns = [
    path('', get_data),
    path('add/', add_book),
    path('get_book/<int:pk>', get_book)
]
