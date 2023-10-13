from proposal.models import Proposal
from django.views.generic.edit import CreateView


class ProposalFormCreate(CreateView):
    model = Proposal
    fields = "__all__"
