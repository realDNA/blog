from django.db import models
from django.contrib.auth import get_user_model
from apps.general.models import Category

User = get_user_model()


class TempArticle(models.Model):
    title = models.CharField(max_length=250)
    category = models.ForeignKey(Category,
                                 related_name="temp_article_categories",
                                 on_delete=models.DO_NOTHING,
                                 default=1,
                                 null=True)
    contents = models.TextField()
    publication_date = models.DateField()
    author = models.ForeignKey(User,
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
    publication_date = models.DateField()
    author = models.ForeignKey(User,
                               related_name="articles",
                               on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.title
