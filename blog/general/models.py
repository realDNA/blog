from django.db import models
from config.script.categorization_loader import load_category_data, get_keys, get_alias
from django.contrib.auth import get_user_model

User = get_user_model()


def create_category_choice():
    category_data = load_category_data()
    keys = get_keys(category_data)
    alias = get_alias(category_data)

    final_choices = ()
    for ali, key in zip(alias, keys):
        final_choices = final_choices + ((ali, key),)

    return final_choices


class Category(models.Model):

    category = models.CharField(
        max_length=20,
        choices=create_category_choice(),
        default=create_category_choice()[0][0]
    )

    def __str__(self):
        return self.category
