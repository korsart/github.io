from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('', main, name='home'),
    path('index/<slug:id>/', index),
    path('categories/', categories),
    re_path(r'^archive/(?P<year>[0-9]{4})/', archive),
]