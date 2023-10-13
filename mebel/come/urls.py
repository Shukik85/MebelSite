from django.urls import path
from come.views import ComePage


app_name = "come"
urlpatterns = [
    path('', ComePage.as_view(), name='come'),
]
