from django import forms
from django.contrib import admin
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.utils.safestring import mark_safe
from works.models import Categoryes, PhotoWorks, Works


class WorksAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Works
        fields = "__all__"


@admin.register(Works)
class WorksAdmin(admin.ModelAdmin):
    form = WorksAdminForm
    list_display = (
        "id",
        "created_at",
        "name",
        "category",
        "client",
        "admin_photo",
    )
    list_display_links = ("name",)
    search_fields = (
        "name",
        "category",
        "client",
    )
    list_filter = (
        "category",
        "created_at",
    )
    fields = (
        "created_at",
        "name",
        "category",
        "description",
        "client",
        "photos",
    )
    readonly_fields = (
        "admin_photo",
        "created_at",
    )

    def admin_photo(self, obj):
        photo = obj.get_photo()
        set_photo = []
        for src in photo:
            width = f'"90px"'
            set_photo += [f'<img src="{src}" width={width}>']
        return mark_safe(set_photo)


@admin.register(PhotoWorks)
class AdminPhoto(admin.ModelAdmin):
    PHOTO = tuple(f"photo{i}" for i in range(1, 7))
    list_display = (
        "created_at",
        "name",
    ) + PHOTO
    list_filter = ("created_at",)
    fields = (
        "created_at",
        "name",
    ) + PHOTO
    readonly_fields = ("created_at",)


@admin.register(Categoryes)
class AdminCategory(admin.ModelAdmin):
    list_display = ("name",)
    fields = ("name",)
