from .models import (
    Category,
    Film, 
    Pictures, 
    Producer, 
    Actor, 
    Hall, 
    Day,
    MovieList
    )
from rest_framework import serializers

class FilmSerializer(serializers.ModelSerializer):

    class Meta:
        model = Film
        fields = '__all__'
        depth = 1

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name', 'slug', 'description')
       
class DaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Day
        fields = ('id' ,'date', 'name')

class MovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieList
        fields = '__all__'
        depth = 1

