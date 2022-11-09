from rest_framework.response import   Response
from rest_framework.views import APIView
from .models import  Movie
from .serializer import MovieSerializer
from rest_framework import generics


class MovieList(generics.ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

