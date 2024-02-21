from django.contrib.auth import authenticate, login, logout
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db import transaction
from django.db.models import Q
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from BookLibrary.BookLibraryAPI.serializers import BooksSerializer, BooksUserSerializer
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


@api_view(['POST'])
@permission_classes([AllowAny])
def register_user(request):
    if request.method == 'POST':
        serializer = BooksUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([AllowAny])
def login_user(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(request, username=username, password=password)

    if user is not None:
        if user.is_active:
            login(request, user)
            return Response({'message': 'Login successful'}, status=200)
        else:
            return Response({'error': 'Account is disabled'}, status=401)
    else:
        return Response({'error': 'Invalid credentials'}, status=401)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout_user(request):
    logout(request)
    return Response({'detail': 'Successfully logged out'}, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def profile_details(request):
    serializer = BooksUserSerializer(request.user)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def edit_user(request):
    user = request.user

    new_username = request.data.get('new_username')
    new_first_name = request.data.get('new_first_name')
    new_last_name = request.data.get('new_last_name')
    new_email = request.data.get('new_email')
    new_gender = request.data.get('new_gender')

    if new_username:
        user.username = new_username
    if new_first_name:
        user.first_name = new_first_name
    if new_last_name:
        user.last_name = new_last_name
    if new_email:
        user.email = new_email
    if new_gender:
        user.gender = new_gender

    user.save()

    return Response({'message': 'User information updated successfully'}, status=200)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def edit_password(request):
    user = request.user

    current_password = request.data.get('current_password')
    new_password = request.data.get('new_password')
    new_password_confirm = request.data.get('new_password_confirm')

    if current_password and not user.check_password(current_password):
        return Response({'error': 'Current password is incorrect'}, status=400)

    if new_password == current_password:
        return Response({'error': 'New password must be different from the current password'}, status=400)

    if new_password and new_password_confirm:
        if new_password == new_password_confirm:
            serializer = BooksUserSerializer(instance=user, data={'password': new_password}, partial=True)

            if serializer.is_valid():
                with transaction.atomic():
                    serializer.save()
                    user.set_password(serializer.validated_data['password'])
                    user.save()

                return Response({'message': 'Password updated successfully'}, status=200)
            else:
                return Response({'error': 'Serializer validation failed', 'details': serializer.errors}, status=400)
        else:
            return Response({'error': 'New passwords do not match'}, status=400)
    else:
        return Response({'error': 'New password and confirmation are required'}, status=400)