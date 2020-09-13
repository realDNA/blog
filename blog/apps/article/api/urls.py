from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.article.api.views import (
        # ArticleListCreateAPIView, ArticleDetailAPIView,
        # TempArticleListCreateAPIView, TempArticleDetailAPIView,
        ArticleViewSet,
        TempArticleViewSet,
)

app_name = 'article-api'

router = DefaultRouter()
router.register(r"articles", ArticleViewSet)
router.register(r"temp/articles", TempArticleViewSet)

urlpatterns = [
    path("", include(router.urls)),
    # path("articles/", ArticleViewSet.as_view(), name="article-list"),
    # path("articles/<int:pk>/", ArticleViewSet.as_view(), name="article-detail"),
    # path("temp/articles/", TempArticleListCreateAPIView.as_view(), name="temp-article-list"),
    # path("temp/articles/<int:pk>/", TempArticleDetailAPIView.as_view(), name="temp-article-detail"),
]
