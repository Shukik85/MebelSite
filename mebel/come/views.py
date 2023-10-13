from django.views.generic import ListView
from home.models import Home
from come.models import Contacts
from proposal.forms import ProposalForm


class ComePage(ListView):
    model = Contacts
    template_name = "come/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = ProposalForm
        context["Home"] = Home.objects.get(is_active=True)
        context["Contact"] = Contacts.objects.all().filter(is_active=True)
        context["title"] = "Контакты"
        return context
