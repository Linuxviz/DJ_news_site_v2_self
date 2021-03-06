# Generated by Django 3.1.5 on 2021-02-14 14:47

import colorfield.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsCategories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название категории')),
                ('description', models.TextField(max_length=150, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='NewsTags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название тега')),
                ('description', models.TextField(max_length=150, verbose_name='Описание')),
                ('background_color', colorfield.fields.ColorField(default='#FF0000', max_length=18)),
                ('text_color', colorfield.fields.ColorField(default='#FF0000', max_length=18)),
            ],
            options={
                'verbose_name': 'Тег',
                'verbose_name_plural': 'Теги',
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Заголовок')),
                ('date_of_create', models.DateTimeField(auto_now=True, verbose_name='Дата создания')),
                ('date_of_last_change', models.DateTimeField(auto_now_add=True, verbose_name='Дата последнего редактирования')),
                ('content', models.TextField(blank=True, verbose_name='Содержание')),
                ('image', models.ImageField(blank=True, upload_to='images/%Y/%m/%d', verbose_name='Изображение')),
                ('published', models.BooleanField(default=True, verbose_name='Статус публикации')),
                ('author_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
                ('category', models.ManyToManyField(related_name='news_category', to='news.NewsCategories')),
                ('tags', models.ManyToManyField(blank=True, related_name='news_tags', to='news.NewsTags')),
            ],
            options={
                'verbose_name': 'Новость',
                'verbose_name_plural': 'Новости',
            },
        ),
    ]
