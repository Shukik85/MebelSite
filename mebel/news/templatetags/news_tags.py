from django.db.models import Count, F
from news.models import Category
from django import template

register = template.Library()

@register.simple_tag(name='get_list_categoryes')
def get_categoryes():
    return Category.objects.all()

@register.inclusion_tag('news/list_categoryes.html')
def show_categoryes():
    # categoryes = Category.objects.all()
    categoryes = Category.objects.annotate(cnt=Count('news', filter=F('news__is_published'))).filter(cnt__gt=0)  # noqa: E501
    # categoryes = Category.objects.annotate(cnt=Count('news')).filter(cnt__gt=0)
    return {'categoryes': categoryes}
