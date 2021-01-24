from django.contrib.auth.models import User  # default user
from django.db import models as m
from colorfield.fields import ColorField  # color picker


class NewsCategories(m.Model):
    """
    EN:
    RU: Категории новостей
    """
    name = m.CharField(max_length=50, verbose_name='Название категории')
    description = m.TextField(max_length=150, verbose_name='Описание')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class NewsTags(m.Model):
    """
    EN:
    RU: Новостные теги
    """
    name = m.CharField(max_length=50, verbose_name='Название тега')
    description = m.TextField(max_length=150, verbose_name='Описание')
    color = ColorField(default='#FF0000')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = "Тег"
        verbose_name_plural = "Теги"


class News(m.Model):
    """
    EN:
    RU: Модель новости, может принадлежать нескольким новостным категориям,
     и содержать в себе разные новостные теги, у новости всегда есть автор
    """
    title = m.CharField(max_length=100, verbose_name='Заголовок')
    author_id = m.ForeignKey(User, on_delete=m.SET_NULL, null=True, verbose_name='Автор')
    date_of_create = m.DateTimeField(auto_now=True, verbose_name='Дата создания')
    date_of_last_change = m.DateTimeField(auto_now_add=True, verbose_name='Дата последнего редактирования')
    content = m.TextField(verbose_name='Содержание', blank=True)
    image = m.ImageField(upload_to='images/%Y/%m/%d', blank=True, verbose_name='Изображение')
    published = m.BooleanField(default=True, verbose_name='Статус публикации')
    category = m.ManyToManyField(NewsCategories, related_name='news_category')
    tags = m.ManyToManyField(NewsTags, blank=True, related_name='news_tags')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"
