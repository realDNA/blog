from django.db import models
from django.contrib.auth.models import User
from apps.general.models import Category


class Article(models.Model):
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
