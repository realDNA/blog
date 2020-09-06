# Set up environment
import os
import sys
import django
sys.path.append('../../../')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "blog.settings")
django.setup()

# Import module
from general.models import Category
from config.script.categorization_loader import load_category_data, get_keys


def initial_category_table(file_name):
    data = load_category_data(file_name)
    keys = get_keys(data)
    print("data = ", data)
    print("keys = ", keys)
    for key in keys:
        if not len(Category.objects.filter(category=key)):
            Category.objects.create(category=key)


if __name__ == "__main__":
    print("start to create category table")
    initial_category_table("catagorization.yml")
    print("finish creating category table")
