from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from rest_framework.response import Response
from rest_framework.decorators import api_view
from BookLibrary.BookLibraryAPI.serializers import BooksSerializer
from BookLibrary.BookLibraryAPI.models import Books


@api_view(['GET'])
def get_data(request):
    books = Books.objects.all()
    serializer = BooksSerializer(books, many=True)

    page = request.query_params.get('page', 1)
    paginator = Paginator(serializer.data, 10)
    try:
        paginated_data = paginator.page(page)
    except PageNotAnInteger:
        paginated_data = paginator.page(1)
    except EmptyPage:
        paginated_data = paginator.page(paginator.num_pages)

    return Response(paginated_data.object_list)


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


@api_view(['GET'])
def search_books(request):
    search_query = request.query_params.get('search', None)

    if search_query:
        queryset = Books.objects.filter(
            Q(headline__icontains=search_query) |
            Q(author__icontains=search_query) |
            Q(description__icontains=search_query)
        )
    else:
        queryset = Books.objects.all()

    serializer = BooksSerializer(queryset, many=True)
    return Response(serializer.data)
