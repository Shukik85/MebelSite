from django.contrib import admin
from proposal.models import Proposal


@admin.register(Proposal)
class ProposalAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "created_at",
        "name",
        "phone",
        "mail",
        "message",
        "files",
    )
    list_display_links = ("name",)
    search_fields = ("name",)
    list_filter = ("created_at",)
    fields = (
        "name",
        "phone",
        "mail",
        "message",
        "files",
    )
