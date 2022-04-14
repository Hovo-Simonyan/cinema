from django.db import models
import datetime


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя")
    slug = models.SlugField(unique=True, db_index=True, verbose_name="Url")
    description = models.TextField(verbose_name="Описание")

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры '

    def __str__(self):
        return self.name

class Film(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя фильма')
    slug = models.SlugField(unique=True, db_index=True, verbose_name="Url")
    description = models.TextField(verbose_name='Описание фильма')
    image = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name="Картинка фильма", blank=True)
    year = models.DateField(verbose_name='День выхода')
    country = models.CharField(max_length=50, verbose_name='Страна производитель')
    budget = models.IntegerField(verbose_name='Бюджет')

    category = models.ManyToManyField('Category')
    producers = models.ManyToManyField('Producer')
    actors = models.ManyToManyField('Actor')


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'
        ordering = ('year',)


class Pictures(models.Model):
    film = models.ForeignKey(Film, on_delete=models.CASCADE, verbose_name='Фильм')
    image = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Картинка')

    class Meta:
        verbose_name = 'Снимок'
        verbose_name_plural = 'Снимкы'
    
    def __str__(self):
        return f'Картинки из фильма - {self.film.name}'


class Producer(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя')
    image = models.ImageField(upload_to='photos/people/%Y/%m/%d/', verbose_name='Картинка')

    class Meta:
        verbose_name = 'Режиссер'
        verbose_name_plural = 'Режиссеры'
    
    def __str__(self):
        return self.name


class Actor(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя')
    image = models.ImageField(upload_to='photos/people/%Y/%m/%d/', verbose_name='Картинка')

    class Meta:
        verbose_name = 'Актер'
        verbose_name_plural = 'Актеры'
    
    def __str__(self):
        return self.name

class Hall(models.Model):
    name = models.CharField(max_length=100, verbose_name='Зал')

    class Meta:
        verbose_name = 'Зал'
        verbose_name_plural = 'Залы'
    
    def __str__(self):
        return self.name


class Day(models.Model):
    date = models.DateField(default = datetime.date.today)
    name = models.CharField(max_length=30, verbose_name='Название дня на армянском')

    class Meta:
        verbose_name = 'День'
        verbose_name_plural = 'Дны'
        ordering = ('date',)

    def __str__(self):
        return f'{self.date}'



class MovieList(models.Model):
    film = models.ForeignKey(Film, on_delete=models.CASCADE, verbose_name='Кино')
    day = models.ForeignKey(Day, on_delete=models.CASCADE, verbose_name='День')
    hall = models.ForeignKey(Hall, on_delete=models.SET_NULL, verbose_name='Зал', null=True)

    date_start = models.DateTimeField('Start Date')
    date_end = models.DateTimeField('End Date')

    language = models.CharField(max_length=20, verbose_name='Язык')
    allow_age = models.SmallIntegerField(verbose_name='Допустимый возраст')
    ticket_coust = models.SmallIntegerField(verbose_name='Цена')
    

    class Meta:
        verbose_name = 'Лист фильма'
        verbose_name_plural = 'Лист фильмов'
        ordering = ('date_start',)

    def __str__(self):
        return self.film.name
