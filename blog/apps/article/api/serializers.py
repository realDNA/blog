from rest_framework import serializers
from apps.article.models import Article, TempArticle


class ArticleSerializer(serializers.ModelSerializer):
    
    author = serializers.StringRelatedField(read_only=True)
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()

    class Meta:
        model = Article
        fields = "__all__"

    def get_created_at(self, instance):
        return instance.created_at.strftime("%B %d, %Y")

    def get_updated_at(self, instance):
        return instance.updated_at.strftime("%B %d, %Y")


class TempArticleSerializer(serializers.ModelSerializer):

    author = serializers.StringRelatedField(read_only=True)
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()

    class Meta:
        model = TempArticle
        fields = "__all__"

    def get_created_at(self, instance):
        return instance.created_at.strftime("%B %d, %Y")

    def get_updated_at(self, instance):
        return instance.updated_at.strftime("%B %d, %Y")

