from django.shortcuts import render
from .serializers import *
from django.db.models import Count
from datetime import datetime
from .models import Category, Film, Pictures, Day, MovieList
from rest_framework import generics


class FilmList(generics.ListCreateAPIView):
    """
    This Api gives you all the films sorted by published year.
    """
    queryset = Film.objects.all()
    serializer_class = FilmSerializer


class CategoryList(generics.ListAPIView):
    """
    This Api gives you all the categories that have films.
    """
    serializer_class = CategorySerializer

    def get_queryset(self):
        return Category.objects.annotate(cnt=Count('film')).filter(cnt__gt=0)


class FilmsByCategory(generics.ListAPIView):
    """
    This Api gives you all the films by exact category.
    """
    serializer_class = FilmSerializer

    def get_queryset(self):
        return Category.objects.filter(
            slug=self.kwargs['category_slug'])[0].film_set.all()


class DaysList(generics.ListAPIView):
    """
    This Api gives you all days from today.
    """
    serializer_class = DaySerializer

    def get_queryset(self):
        now = datetime.now()
        day = now.strftime("%d")
        month = now.strftime("%m")

        return Day.objects.filter(date__day__gte=day, date__month__gte=month)


class FilmsByDay(generics.ListAPIView):
    """
    This Api gives you all the films by exact day sorted with date_start.
    """
    serializer_class = MovieListSerializer

    def get_queryset(self):
        return Day.objects.get(
            pk=self.kwargs['day_id']).movielist_set.order_by('date_start')
