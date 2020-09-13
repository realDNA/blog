from django.db import models
from django.conf import settings
from apps.general.models import Category


class TempArticle(models.Model):
    title = models.CharField(max_length=250)
    category = models.ForeignKey(Category,
                                 related_name="temp_article_categories",
                                 on_delete=models.DO_NOTHING,
                                 default=1,
                                 null=True)
    contents = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    slug = models.SlugField(max_length=255,
                            default='',
                            editable=False,
                            unique=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               related_name="temp_articles",
                               on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.title


class Article(models.Model):
    drafted_article = models.ForeignKey(TempArticle,
                                        related_name="article_temp_saved",
                                        on_delete=models.DO_NOTHING,
                                        null=True)
    title = models.CharField(max_length=250)
    category = models.ForeignKey(Category,
                                 related_name="article_categories",
                                 on_delete=models.DO_NOTHING,
                                 default=1,
                                 null=True)
    contents = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    slug = models.SlugField(max_length=255,
                            default='',
                            editable=False,
                            unique=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               related_name="articles",
                               on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.title
