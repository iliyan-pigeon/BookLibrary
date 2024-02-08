from django.urls import path

from BookLibrary.BookLibraryFrontend.views import index

urlpatterns = [
    path('', index, name='index')
]
