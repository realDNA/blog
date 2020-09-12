from rest_framework import serializers
from apps.article.models import Article, TempArticle


class ArticleSerializer(serializers.ModelSerializer):
    
    author = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Article
        fields = "__all__"


class TempArticleSerializer(serializers.ModelSerializer):

    author = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = TempArticle
        fields = "__all__"
