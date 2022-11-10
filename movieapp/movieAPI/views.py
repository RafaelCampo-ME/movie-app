from .models import  Movie
from .serializer import MovieSerializer
from rest_framework import generics
from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from rest_framework.response import Response


class MovieList(generics.ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class PostMovie(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class createMovie(ModelViewSet):
    """_summary_

    Args:
        ModelViewSet (_type_): _description_

    Returns:
        _type_: _description_
        https://ilovedjango.com/django/rest-api-framework/views/tips/sub/modelviewset-django-rest-framework/
        https://www.django-rest-framework.org/api-guide/viewsets/#modelviewset
        https://ilovedjango.com/django/rest-api-framework/create-data-using-api/
    """
    queryset = Movie.objects.none()
    serializer_class = MovieSerializer
    http_method_names = ['post',]

    def create(self, request, *arg, **kwargs):
        user = request.user
        data = {
            "title":request.Movie.get('title',None)
        }
        serializer = self.serializer_class(data=data, contex = {'author':user})
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

