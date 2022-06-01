from distutils.command.upload import upload
from django.db import models

class Authors(models.Model):
    first_name = models.CharField(max_length=25, verbose_name='Имя')
    second_name = models.CharField(max_length=25, verbose_name='Фамилия')
    patronymic = models.CharField(max_length=25, verbose_name='Отчество', blank=True)
    length_of_service = models.CharField(max_length=50, verbose_name='Стаж работы', blank=True)
   # is_published = models.BooleanField(default=True)
    # country = models.ForeignKey('Countries', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.second_name

class Tegs(models.Model):
    title = models.CharField(max_length=50, verbose_name='Тег')

    def __str__(self):
        return self.title

class Books(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название книги')
    description = models.CharField(max_length=300, verbose_name='Описание книги')
    image = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    author = models.ManyToManyField(Authors)
    teg = models.ManyToManyField(Tegs)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title