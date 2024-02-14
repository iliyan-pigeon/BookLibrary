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

    def create(self, validated_data):
        user = BooksUser(
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            email=validated_data['email'],
            gender=validated_data['gender'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
