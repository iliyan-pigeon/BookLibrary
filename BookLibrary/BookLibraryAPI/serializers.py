from rest_framework import serializers
from BookLibrary.BookLibraryAPI.models import Books, BooksUser


class BooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = '__all__'


class BooksUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = BooksUser
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'gender', 'password']
        extra_kwargs = {'password': {'write_only': True}}
