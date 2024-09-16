from rest_framework import serializers
from .models import Author, Book, Publisher,Review


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name', 'bio']
        read_only_fields = ['id']
        
class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)
    publisher = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'publication_date', 'price', 'stock', 'publisher']
        read_only_fields = ['id']

class PublisherSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Publisher
        fields = ['id', 'name', 'address', 'books']
        read_only_fields = ['id']
        
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'book', 'rating', 'comment']
        read_only_fields = ['id']