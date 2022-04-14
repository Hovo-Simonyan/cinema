from django.contrib import admin
from .models import *
# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    list_display_links = ('id', 'name')
    prepopulated_fields = {"slug": ("name", )}


class FilmAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'year', 'country', 'budget')
    list_display_links = ('id', 'name')
    prepopulated_fields = {"slug": ("name", )}


class PicturesAdmin(admin.ModelAdmin):
    list_display = ('id', 'film')
    list_display_links = ('id',)


class ProducerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')


class ActorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')


class HallAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')

class DayAdmin(admin.ModelAdmin):
    list_display = ('id', 'date', 'name')
    list_display_links = ('id', 'name')

class MovieListAdmin(admin.ModelAdmin):
    list_display = ('id', 'hall', 'language', 'allow_age', 'ticket_coust')
    list_display_links = ('id',)



admin.site.register(Category, CategoryAdmin)
admin.site.register(Film, FilmAdmin)
admin.site.register(Pictures, PicturesAdmin)
admin.site.register(Producer, ProducerAdmin)
admin.site.register(Actor, ActorAdmin)
admin.site.register(Hall, HallAdmin)
admin.site.register(Day, DayAdmin)
admin.site.register(MovieList, MovieListAdmin)
