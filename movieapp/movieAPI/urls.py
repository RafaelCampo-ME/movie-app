from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import MovieList, PostMovie

urlpatterns = [
    path('', MovieList.as_view(),name="Movie_list"),
    path('id:<int:pk>/',PostMovie.as_view())
]
