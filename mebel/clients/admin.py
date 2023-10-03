from django.contrib import admin
from clients.models import Clients


@admin.register(Clients)
class ClientsAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "created_at",
        "name",
        "adress",
        "phone",
        "mail",
    )
    list_display_links = ("name",)
    search_fields = (
        "name",
        "phone",
    )
    readonly_fields = ("created_at",)
    fields = (
        "created_at",
        "name",
        "adress",
        "phone",
        "mail",
    )
