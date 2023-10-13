from django.contrib import admin
from come.models import Contacts




@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "is_active",
        "name",
        "adress",
        "phone",
        "mail",
        "url",
    )
    list_display_links = ("name",)
    search_fields = ("name",)
    list_filter = ("is_active",)
    fields = (
        "is_active",
        "name",
        "adress",
        "phone",
        "mail",
        "url",
    )
