from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import MovieList

urlpatterns = [
    path('list', MovieList.as_view(),name="Movie_list")
]
