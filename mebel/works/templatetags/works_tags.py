from django.db.models import Count
from works.models import Categoryes
from django import template

register = template.Library()


@register.inclusion_tag("works/inc/_list_categoryes.html")
def show_categoryes():
    if Categoryes:
        categoryes = Categoryes.objects.annotate(cnt=Count("works")).filter(cnt__gt=0)
    else:
        categoryes = []
    return {"categoryes": categoryes}
