from django.contrib import admin
from django.utils.safestring import mark_safe
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from news.models import News
from news.models import Category


class NewsAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = News
        fields = "__all__"


class NewsAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "category",
        "author",
        "title",
        "content",
        "created_at",
        "get_photo",
        "is_published",
    )
    list_display_links = (
        "id",
        "title",
    )
    search_fields = (
        "title",
        "content",
    )
    list_filter = (
        "id",
        "is_published",
    )
    list_editable = (
        "category",
        "is_published",
    )
    fields = (
        "category",
        "title",
        "content",
        "photo",
        "get_photo",
        "is_published",
        "author",
        "created_at",
        "updated_at",
    )
    readonly_fields = ("get_photo", "author", "created_at", "updated_at")
    form = NewsAdminForm

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="90px">')
        else:
            return "Фото нет"

    get_photo.short_description = "Минитюра"

    def save_model(self, request, obj, form, change):
        if not change:
            obj.author = request.user

        super(NewsAdmin, self).save_model(
            request=request, obj=obj, form=form, change=change
        )


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
    )
    list_display_links = (
        "id",
        "title",
    )
    search_fields = ("title",)


admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoryAdmin)

admin.site.site_title = "Страница администратора"
admin.site.site_header = "Страница администратора"
