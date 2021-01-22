# Generated by Django 3.1.5 on 2021-01-22 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='date_of_create',
            field=models.DateTimeField(auto_now=True, verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='news',
            name='date_of_last_change',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата последнего редактирования'),
        ),
        migrations.AlterField(
            model_name='news',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/%Y/%m/%d', verbose_name='Изображение'),
        ),
    ]
