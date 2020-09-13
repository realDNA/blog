from rest_framework import generics, status, viewsets
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated
from apps.article.models import Article, TempArticle
from apps.article.api.serializers import ArticleSerializer, TempArticleSerializer
from apps.article.api.permissions import IsAdminUser, IsAdminUserOrReadOnly


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    lookup_field = "slug"  # can use lookup_field field to search endpoint like api/article/slug
    serializer_class = ArticleSerializer
    permission_classes = [IsAuthenticated, IsAdminUserOrReadOnly]

    def perform_create(self, serializer):
        try:
            author = self.request.user
            serializer.save(author=author)
        except Exception:
            raise ValidationError("Please log in")


class TempArticleViewSet(viewsets.ModelViewSet):
    queryset = TempArticle.objects.all()
    serializer_class = TempArticleSerializer
    permission_classes = [IsAdminUser]

    def perform_create(self, serializer):
        try:
            author = self.request.user
            serializer.save(author=author)
        except Exception:
            raise ValidationError("Please log in")


# class ArticleListCreateAPIView(generics.ListCreateAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer
#     permission_classes = [IsAdminUserOrReadOnly]
#
#     def perform_create(self, serializer):
#         try:
#             author = self.request.user
#             serializer.save(author=author)
#         except Exception:
#             raise ValidationError("Please log in")
#
#
# class ArticleDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer


# class TempArticleListCreateAPIView(generics.ListCreateAPIView):
#     queryset = TempArticle.objects.all()
#     serializer_class = TempArticleSerializer
#     permission_classes = [IsAdminUser]
#
#     def perform_create(self, serializer):
#         try:
#             author = self.request.user
#             serializer.save(author=author)
#         except Exception:
#             raise ValidationError("Please log in")
#
#
# class TempArticleDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = TempArticle.objects.all()
#     serializer_class = TempArticleSerializer
