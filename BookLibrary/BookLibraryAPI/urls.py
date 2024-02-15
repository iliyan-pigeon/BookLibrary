from django.urls import path
from BookLibrary.BookLibraryAPI.views import get_data, add_book, get_book, update_book, delete_book, search_books, \
    register_user, login_user, logout_user, profile_details

urlpatterns = [
    path('', get_data, name='get data'),
    path('add-book/', add_book, name='add book'),
    path('get-book/<int:pk>', get_book, name='get book'),
    path('update-book/<int:pk>', update_book, name='update book'),
    path('delete-book/<int:pk>', delete_book, name='delete book'),
    path('search-books/', search_books, name='search books'),
    path('register/', register_user, name='register user'),
    path('login/', login_user, name='login user'),
    path('logout/', logout_user, name='logout user'),
    path('profile-details/', profile_details, name="profile details")
]
