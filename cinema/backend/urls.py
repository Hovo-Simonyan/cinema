from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('films/', FilmList.as_view()),
    path('categories/', CategoryList.as_view()),
    path('filmsbycategory/<slug:category_slug>/', FilmsByCategory.as_view()),
    path('days/', DaysList.as_view()),
    path('daylist/<int:day_id>/', FilmsByDay.as_view()),
    path('api-auth/', include('rest_framework.urls')),
]



