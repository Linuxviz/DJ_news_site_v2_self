from django.urls import path
from .views import HomePageView, NewsDetailView

urlpatterns = [
    path('', HomePageView.as_view(), name='home_page'),
    path('news/<int:index>/', NewsDetailView.as_View(), name='news_detail_page'),
]
