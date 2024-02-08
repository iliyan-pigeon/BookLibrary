from rest_framework.response import Response
from rest_framework.decorators import api_view
from BookLibrary.BookLibraryAPI.serializers import BooksSerializer
from BookLibrary.BookLibraryAPI.models import Books


@api_view(['GET'])
def get_data(request):
    books = Books.objects.all()
    serializer = BooksSerializer(books, many=True)

    return Response(serializer.data)


@api_view(['POST'])
def add_book(request):
    serializer = BooksSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['GET'])
def get_book(request, pk):
    book = Books.objects.get(id=pk)
    serializer = BooksSerializer(book, many=False)

    return Response(serializer.data)


@api_view(['POST'])
def update_book(request, pk):
    book = Books.objects.get(id=pk)
    serializer = BooksSerializer(instance=book, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
def delete_book(request, pk):
    book = Books.objects.get(id=pk)
    book.delete()

    return Response(f'The "{book.headline}" book is deleted!')
