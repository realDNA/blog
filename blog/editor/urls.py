from django.urls import path, re_path
from . import views

app_name = 'editor'

urlpatterns = [
    path('article/new', views.CreatePost.as_view(), name='create_article'),
]
