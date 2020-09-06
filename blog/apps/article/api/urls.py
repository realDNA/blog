from django.urls import path
from apps.article.api.views import (ArticleListCreateAPIView, ArticleDetailAPIView)

app_name = 'editor-api'

urlpatterns = [
    path("articles/", ArticleListCreateAPIView.as_view(), name="article-list"),
    path("articles/<int:pk>/", ArticleDetailAPIView.as_view(), name="article-detail"),
]
