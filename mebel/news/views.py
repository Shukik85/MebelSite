from django.views.generic import CreateView, DetailView, ListView
from news.forms import NewsForm
from news.models import News, Category
from django.contrib.auth.mixins import LoginRequiredMixin
from news.utils import MyMixin


class HomeNews(ListView, MyMixin):
    model = News
    context_object_name = "news"
    template_name = "news/index.html"
    extra_context = {"title": "Главная"}
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Главная"
        return context

    def get_queryset(self):
        return News.objects.filter(is_published=True).select_related("category")


class NewsByCategory(ListView):
    model = News
    context_object_name = "news"
    template_name = "news/category.html"
    allow_empty = False
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = Category.objects.get(pk=self.kwargs["category_id"]).title
        return context

    def get_queryset(self):
        return News.objects.filter(
            category_id=self.kwargs["category_id"], is_published=True
        ).select_related("category")


class ViewNews(DetailView):
    model = News
    template_name = "news/news.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = News.objects.get(pk=self.kwargs["pk"]).title
        return context


class AddNews(LoginRequiredMixin, CreateView):
    model = News
    form_class = NewsForm
    template_name = "news/add_news.html"
    extra_context = {"title": "Добавить новость"}
    login_url = "admin/"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
