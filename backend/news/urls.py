from django.urls import path
from news import views

app_name = 'news'

urlpatterns = [
    path('', views.show_news_view, name='show_news'),
    path('<int:news_id>/', views.news_detail_view, name='news'),
]