from dataclasses import fields
from rest_framework import serializers
from .models import Authors, Books, Tegs

class AuthorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Authors
        fields = ('first_name', 'second_name')

class TegsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tegs
        fields = ('title',)

class BooksSerializer(serializers.ModelSerializer):
    author = AuthorsSerializer(many=True)
    teg = TegsSerializer(many=True)
    class Meta:
        model = Books
        fields = ('title', 'author', 'teg')

class BooksSerializer2(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = ('title', 'author', 'teg')