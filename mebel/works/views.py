from django.views.generic import DetailView, ListView
from come.models import Contacts
from works.models import Categoryes, Works


class WorksPage(ListView):
    model = Works
    paginate_by = 5
    context_object_name = "Works"
    template_name = "works/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Наши работы"
        context["Contact"] = Contacts.objects.all().filter(is_active=True)
        return context


class WorksByCategory(ListView):
    model = Works
    context_object_name = "Works"
    template_name = "works/index.html"
    allow_empty = False
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = Categoryes.objects.get(pk=self.kwargs["pk"]).name
        context["Contact"] = Contacts.objects.all().filter(is_active=True)
        return context

    def get_queryset(self):
        return Works.objects.filter(category_id=self.kwargs["pk"]).select_related(
            "category"
        )


class WorkView(DetailView):
    model = Works
    template_name = "works/work.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = Works.objects.get(pk=self.kwargs["pk"]).name
        context["Contact"] = Contacts.objects.all().filter(is_active=True)
        return context
