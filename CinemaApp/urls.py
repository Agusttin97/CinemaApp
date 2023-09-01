from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name="Home"),
    path('cinema', cinema, name="Cinema"),
    path('movie', movie, name="Movie"),
    path('user', user, name="User"),
    path('search-movie', searchMovie, name="SearchMovie"),
    path('search', search, name="Search"),
]