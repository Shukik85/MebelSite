from django.urls import path
from proposal.views import ProposalFormCreate


app_name = "proposal"
urlpatterns = [
    path("", ProposalFormCreate.as_view(), name="create"),
]
