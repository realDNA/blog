from rest_framework import generics
from rest_framework.exceptions import ValidationError
from apps.article.models import Article, TempArticle
from apps.article.api.serializers import ArticleSerializer, TempArticleSerializer


class ArticleListCreateAPIView(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def perform_create(self, serializer):
        try:
            author = self.request.user
            serializer.save(author=author)
        except Exception:
            raise ValidationError("Please log in")


class ArticleDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class TempArticleListCreateAPIView(generics.ListCreateAPIView):
    queryset = TempArticle.objects.all()
    serializer_class = TempArticleSerializer

    def perform_create(self, serializer):
        try:
            author = self.request.user
            serializer.save(author=author)
        except Exception:
            raise ValidationError("Please log in")


class TempArticleDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TempArticle.objects.all()
    serializer_class = TempArticleSerializer
