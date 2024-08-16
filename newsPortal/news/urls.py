from django.urls import path
from . import views

urlpatterns = [
    # Существующие маршруты
    path('', views.news_list, name='news_list'),
    path('<int:article_id>/', views.news_detail, name='news_detail'),

    # Маршруты для новостей
    path('news/create/', views.NewsCreateView.as_view(), name='news_create'),
    path('news/<int:pk>/edit/', views.NewsUpdateView.as_view(), name='news_edit'),
    path('news/<int:pk>/delete/', views.NewsDeleteView.as_view(), name='news_delete'),

    # Маршруты для статей
    path('articles/create/', views.ArticleCreateView.as_view(), name='article_create'),
    path('articles/<int:pk>/edit/', views.ArticleUpdateView.as_view(), name='article_edit'),
    path('articles/<int:pk>/delete/', views.ArticleDeleteView.as_view(), name='article_delete'),

    # Другие существующие маршруты (если есть)
    # path('other-url/', views.OtherView.as_view(), name='other_view'),
]


