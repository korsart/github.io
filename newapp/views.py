from django.http import Http404, HttpResponse, HttpResponseNotFound
from django.shortcuts import redirect, render
from rest_framework import generics, filters
from .serializers import *
from .models import Authors, Books, Tegs
from rest_framework.views import APIView
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

class AuthorsAPIList(generics.ListCreateAPIView):
    queryset = Authors.objects.all()
    serializer_class = AuthorsSerializer

class BooksAPIList(generics.ListCreateAPIView):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['author', 'teg']
    search_fields = ['title', 'description', 'author', 'teg']
    ordering_fields = '__all__'

    def get_serializer_class(self):
        if self.request.method == "POST":
            return BooksSerializer2
        elif self.request.method == "GET":
            return BooksSerializer

class BooksAPIDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer
    