from django import forms
from django.contrib import admin
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.utils.safestring import mark_safe
from home.models import Card, Contacts, Home


class HomeAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget)

    class Meta:
        model = Home
        fields = "__all__"


@admin.register(Home)
class HomeAdmin(admin.ModelAdmin):
    form = HomeAdminForm
    BASE = (
        "offer",
        "info",
        "advantage",
        "works",
        "made",
        "partnership",
        "accordeon",
    )
    list_display = (
        "id",
        "is_active",
        "created_at",
        "name",
        "description",
    )
    list_display_links = ("name",)
    search_fields = (
        "name",
        "description",
    )
    list_filter = (
        "created_at",
        "is_active",
    )
    fields = (
        "created_at",
        "is_active",
        "name",
        "description",
    ) + BASE
    readonly_fields = ("created_at",)


class CardAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget)

    class Meta:
        model = Card
        fields = "__all__"


@admin.register(Card)
class CardHomeAdmin(admin.ModelAdmin):
    form = CardAdminForm
    list_display = (
        "id",
        "created_at",
        "version",
        "category",
        "title",
        "get_img",
    )
    list_display_links = ("title",)
    search_fields = ("version",)
    list_filter = (
        "created_at",
        "category",
        "version",
    )
    fields = (
        "created_at",
        "version",
        "category",
        "title",
        "img",
        "description",
        "get_img",
    )
    readonly_fields = (
        "created_at",
        "get_img",
    )

    def get_img(self, obj):
        if obj.img:
            img = mark_safe(f'<img src="{obj.img.url}" width="90px">')
            return img
        else:
            return "Фото нет"

    get_img.short_description = "Минитюра"


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
