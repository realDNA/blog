from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from apps.article.models import Article
from .forms import ArticleForm
# Create your views here.


class CreatePost(LoginRequiredMixin, CreateView):
    model = Article
    template_name = "editor/editor_form.html"
    form_class = ArticleForm
