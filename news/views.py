from django.db.models import Q
from django.views.generic import ListView, DetailView

from .models import News, NewsCategories, NewsTags


class GetContextForSideBar:
    def get_context_data(self, **kwargs):
        """
        RU:В контексте передаю название категорий и количество новостей которые принаддежат к той,
         или иной категории. Неоптимально, уверен можно сделать лучше но ничего не нашел. ВАЖНО!
        объявление должно быть до ListView т.к. перегружает метод именно этого объекта
        EN:the declaration must be before the ListView
         because overloads the method of this particular object
        """
        context = super().get_context_data(**kwargs)
        context['categories_count'] = {}
        for category in NewsCategories.objects.all():
            context['categories_count'][category.name] = (News.objects.filter(category__name=category).count())
        # print(context)
        return context


class HomePageView(GetContextForSideBar, ListView):
    """
    RU: Контроллер основной страницы, выводит новости и список категорий с количеством новостей в них,
    используется пагинатор
    EN:
    """
    model = News
    template_name = 'news/home_template.html'
    queryset = News.objects.filter(published=True)
    paginate_by = 8


class NewsDetailView(GetContextForSideBar, DetailView):
    model = News
    template_name = 'news/news_detail_template.html'


class NewsByCategoryView(GetContextForSideBar, ListView):
    model = News
    template_name = 'news/news_by_category_template.html'
    paginate_by = 8

    def get_queryset(self):
        return News.objects.filter(
            Q(category__name=self.kwargs['category_name']) &
            Q(published=True)
        )

    def get_context_data(self, **kwargs):
        """
        RU: Добавляет имя активной категории
        EN:
        """
        context = super().get_context_data(**kwargs)
        context['current_category'] = self.kwargs['category_name']
        return context


class NewsByTagView(GetContextForSideBar, ListView):
    model = News
    template_name = 'news/news_by_tag_template.html'
    paginate_by = 8

    def get_queryset(self):
        return News.objects.filter(
            Q(tags__name=self.kwargs['tag_name']) &
            Q(published=True)
        )
