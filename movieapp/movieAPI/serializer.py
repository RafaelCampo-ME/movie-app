from rest_framework import serializers
from .models import Movie

class MovieSerializer(serializers.ModelSerializer):
    
    def create(self, validated_data):
        title = validated_data.get(title)
        validated_data['author'] = self.context['author'] # optional , saving extra data
        post = Movie.objects.create(**validated_data) 
        return post



    class Meta:
        model = Movie
        fields = ('__all__')