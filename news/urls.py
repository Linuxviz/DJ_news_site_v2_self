from django.urls import path
from .views import HomePageView, NewsDetailView, NewsByCategoryView, NewsByTagView

urlpatterns = [
    path('', HomePageView.as_view(), name='home_page'),
    path('newsByCategory/<str:category_name>/', NewsByCategoryView.as_view(), name='news_by_category'),
    path('newsByTag/<str:tag_name>/', NewsByTagView.as_view(), name='news_by_tag'),
    path('news/<int:pk>/', NewsDetailView.as_view(), name='news_detail_page'),
]
