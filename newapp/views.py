from django.http import Http404, HttpResponse, HttpResponseNotFound
from django.shortcuts import redirect, render
from rest_framework import generics, filters
from .serializers import *
from .models import Authors, Books, Tegs
from rest_framework.views import APIView
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend


def index(request, id):
    if(request.GET):
        print(request.GET)
    return HttpResponse(f'<h2>Index</h2><p>{id}</p>')

def categories(request):
    if(request.GET):
        print(request.GET)
    return HttpResponse('Categories')

def main(request):
    if(request.GET):
        print(request.GET)
    return HttpResponse('<h1>Main</h1>') 


def archive (request, year):
    if(request.GET):
        print(request.GET)
    if int(year) > 2022:
        return redirect('home')
    return HttpResponse(f'<h1>Архив по годам</h1><p>{year}</p>')

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>ОШИБКА ЧЕТЫРЕСТАЧЕТЫРЕ ЁПТА</h1><h2>НА ЭТОЙ СТРАНИЦЕ НИХУЯ НЕТ</h2><h3>Постарайтесь больше так не проёбываться</h3>')


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
    