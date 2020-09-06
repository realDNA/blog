from django.shortcuts import render
from django.views.generic import CreateView
from article.models import Article
from .forms import ArticleForm
# Create your views here.


class CreatePost(CreateView):
    model = Article
    template_name = "editor/editor_form.html"
    form_class = ArticleForm
