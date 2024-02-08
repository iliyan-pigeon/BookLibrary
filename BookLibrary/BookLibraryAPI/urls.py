from django.urls import path
from BookLibrary.BookLibraryAPI.views import get_data, add_book, get_book

urlpatterns = [
    path('', get_data, name='get data'),
    path('add-book/', add_book, name='add book'),
    path('get-book/<int:pk>', get_book, name='get book')
]
