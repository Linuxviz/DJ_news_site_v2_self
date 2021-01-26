from django.urls import path
from .views import HomePageView, NewsDetailView, NewsByCategory

urlpatterns = [
    path('', HomePageView.as_view(), name='home_page'),
    path('news/<int:pk>/', NewsDetailView.as_view(), name='news_detail_page'),
    path('newsByCategory/<str:category_name>/', NewsByCategory.as_view(), name='news_by_category'),
]
