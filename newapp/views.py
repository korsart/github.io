from django.shortcuts import redirect, render
from rest_framework import generics, filters

from .permissions import IsAdminAndManagerOrReadOnly, IsAdminAndAuthorOrReadOnly
from .serializers import *
from .models import Books, User
from rest_framework.permissions import *
from django_filters.rest_framework import DjangoFilterBackend

class BooksAPIList(generics.ListAPIView):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['author', 'teg']
    search_fields = ['title', 'description', 'author', 'teg']
    ordering_fields = '__all__'

class BooksAPICreate(generics.ListCreateAPIView):
    queryset = Books.objects.all()
    serializer_class = BooksCreateSerializer
    permission_classes = (IsAuthenticated,)

class BooksAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['author', 'teg']
    search_fields = ['title', 'description', 'author', 'teg']
    ordering_fields = '__all__'
    permission_classes = (IsAdminAndManagerOrReadOnly)

    def get_serializer_class(self):
        if self.request.method == "POST":
            return BooksSerializer2
        elif self.request.method == "GET":
            return BooksSerializer

class BooksAPIDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer
    permission_classes = (IsAdminAndAuthorOrReadOnly)

class UserAPIDetail(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAdminAndAuthorOrReadOnly)

class UserAPICreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer