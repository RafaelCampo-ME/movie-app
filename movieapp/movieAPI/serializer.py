from rest_framework import serializers
from .models import Movie

class MovieSerializer(serializers.ModelSerializer):
    
   # title = serializers.CharField()
   # director_name = serializers.CharField()
   # ticket_price = serializers.FloatField()
   # 
   # 
   # def create(self, validated_data):
   #     title = validated_data.get(title)
   #     validated_data['author'] = self.context['author'] # optional , saving extra data
   #     post = Movie.objects.create(**validated_data) 
   #     return post

    class Meta:
        model = Movie
        fields = ['title','director_name','ticket_price']