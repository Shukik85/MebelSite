from django.views.generic import CreateView, DetailView, ListView
from news.forms import NewsForm
from news.models import News, Category
from news.utils import MyMixin


class HomeNews(ListView, MyMixin):
    model = News
    context_object_name = "news"
    template_name = "News/index.html"
    extra_context = {"title": "Главная"}
    paginate_by = 2

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Главная"
        return context

    def get_queryset(self):
        return News.objects.filter(is_published=True).select_related("category")


class NewsByCategory(ListView):
    model = News
    context_object_name = "news"
    template_name = "News/category.html"
    allow_empty = False
    paginate_by = 2

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
    template_name = "News/news.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = News.objects.get(pk=self.kwargs["pk"]).title
        return context


class AddNews(CreateView):
    form_class = NewsForm
    template_name = "News/add_news.html"
    extra_context = {"title": "Добавить новость"}
    login_url = "admin/"
