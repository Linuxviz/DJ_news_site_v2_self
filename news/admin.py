from django.contrib import admin
from .models import News, NewsTags, NewsCategories

admin.site.register(News)
admin.site.register(NewsTags)
admin.site.register(NewsCategories)
