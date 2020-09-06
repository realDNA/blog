from rest_framework import generics
from rest_framework.exceptions import ValidationError
from apps.article.models import Article
from apps.article.api.serializers import ArticleSerializer


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
