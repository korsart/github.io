# Generated by Django 4.0.4 on 2022-06-01 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Authors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=25, verbose_name='Имя')),
                ('second_name', models.CharField(max_length=25, verbose_name='Фамилия')),
                ('patronymic', models.CharField(blank=True, max_length=25, verbose_name='Отчество')),
                ('length_of_service', models.CharField(blank=True, max_length=50, verbose_name='Стаж работы')),
            ],
        ),
        migrations.CreateModel(
            name='Tegs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Тег')),
            ],
        ),
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название книги')),
                ('description', models.CharField(max_length=300, verbose_name='Описание книги')),
                ('image', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('time_create', models.DateTimeField(auto_now_add=True)),
                ('time_update', models.DateTimeField(auto_now=True)),
                ('author', models.ManyToManyField(to='newapp.authors')),
                ('teg', models.ManyToManyField(to='newapp.tegs')),
            ],
        ),
    ]
