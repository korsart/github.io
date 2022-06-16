from django.urls import path
from .views import *

urlpatterns = [
    
    path('bookslist/', BooksAPIList.as_view()),
    path('booksdetail/<int:pk>/', BooksAPIDetail.as_view()),
    path('booksupdate/<int:pk>/', BooksAPIUpdate.as_view()),
    path('userdetail/<int:pk>/', UserAPIDetail.as_view()),
    path('bookscreate/', BooksAPICreate.as_view()),
    path('usercreate/', UserAPICreate.as_view()),
]