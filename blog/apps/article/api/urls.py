from django.urls import path
from apps.article.api.views import (ArticleListCreateAPIView, ArticleDetailAPIView
                                    , TempArticleListCreateAPIView, TempArticleDetailAPIView)

app_name = 'article-api'

urlpatterns = [
    path("articles/", ArticleListCreateAPIView.as_view(), name="article-list"),
    path("articles/<int:pk>/", ArticleDetailAPIView.as_view(), name="article-detail"),
    path("temp/articles/", TempArticleListCreateAPIView.as_view(), name="temp-article-list"),
    path("temp/articles/<int:pk>/", TempArticleDetailAPIView.as_view(), name="temp-article-detail"),
]
