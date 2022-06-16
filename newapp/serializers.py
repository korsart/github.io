from dataclasses import fields
from rest_framework import serializers
from .models import Books, Tegs, User

class TegsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tegs
        fields = ('title',)

class BooksCreateSerializer(serializers.ModelSerializer):
    #teg = TegsSerializer(many=True)
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Books
        fields = ('title', 'author', 'teg')

class BooksSerializer(serializers.ModelSerializer):
    teg = TegsSerializer(many=True)
    class Meta:
        model = Books
        fields = ('title', 'author', 'teg')

class BooksSerializer2(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = ('title', 'author', 'teg')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('name', 'email', 'phone_number')

class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('name', 'email', 'password')
    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        user.set_password(validated_data.get("password"))
        user.save()
        return user

