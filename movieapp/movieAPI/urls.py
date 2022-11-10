from django.urls import path, include
from rest_framework import routers
from .views import MovieList, PostMovie,createMovie

router = routers.DefaultRouter()
router.register(r'custom-viewset',createMovie)

urlpatterns = [
    path('', MovieList.as_view(),name="Movie_list"),
    path('id:<int:pk>/',PostMovie.as_view()),
    path('crud',include(router.urls)) # maybe we need to use 
]
