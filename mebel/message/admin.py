from django.contrib import admin
from message.models import Message


@admin.register(Message)
class AdminMessage(admin.ModelAdmin):
    list_display = ("sender", "msg", "recipient")
    fields = ("sender", "msg", "recipient")
    readonly_fields = ("sender",)
