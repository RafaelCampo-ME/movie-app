from .models import  Movie
from .serializer import MovieSerializer
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import JSONParser  



class MovieList(generics.ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class PostMovie(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

@api_view(['GET','POST'])
def newMovie( request):
    """
    Lista a todas la peliculas

    Args:
        request (_type_): _description_
    """
    if request.method == 'GET':
        queryset = Movie.objects.all()
        serializer = MovieSerializer(queryset, many = True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        jsonData = JSONParser().parse(request)
        serializer = MovieSerializer(data = jsonData)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, safe = False)



