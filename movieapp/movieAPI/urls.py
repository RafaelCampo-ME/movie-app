from django.urls import path, include
from rest_framework import routers
from .views   import MovieList, PostMovie , newMovie

 

urlpatterns = [
    path('', MovieList.as_view(),name="Movie_list"),
    path('id:<int:pk>/',PostMovie.as_view()),
    path('crud',newMovie) # maybe we need to use 
]

