from django.views.generic import ListView
from come.models import Contacts
from home.models import Home
from proposal.forms import ProposalForm


class HomePage(ListView):
    model = Home
    context_object_name = "Home"
    template_name = "home/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = ProposalForm
        context["Contact"] = Contacts.objects.all().filter(is_active=True)
        context["title"] = "Главная"
        return context

    def get_queryset(self):
        return Home.objects.get(is_active=True)
