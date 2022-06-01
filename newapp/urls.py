from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('authorslist/', AuthorsAPIList.as_view()),
    path('bookslist/', BooksAPIList.as_view()),
    path('booksdetail/<int:pk>/', BooksAPIDetail.as_view()),
]