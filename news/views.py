from django.views.generic import ListView, DetailView
from django.views.generic.base import View

from .models import News, NewsCategories, NewsTags


class HomePageView(ListView):
    """
    RU: Контроллер основной страницы, выводит новости и список категорий с количеством новостей в них,
    используется пагинатор
    EN:
    """
    model = News
    template_name = 'news/home_template.html'
    queryset = News.objects.filter(published=True)
    paginate_by = 8

    def get_context_data(self, **kwargs):
        """В контексте передаю название категорий и количество новостей которые принаддежат к той,
         или иной категории. Неоптимально, уверен можно сделать лучше но ничего не нашел, еще кажется QS
         дважды отправляется"""
        context = super().get_context_data(**kwargs)
        context['categories_count'] = {}
        for category in NewsCategories.objects.all():
            context['categories_count'][category.name] = (News.objects.filter(category__name=category).count())
        # print(context)
        return context


class NewsDetailView(DetailView):
    model = News
    template_name = 'news/news_detail_template.html'

