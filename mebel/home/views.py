from django.shortcuts import render
from django.views.generic import CreateView, DetailView, ListView

from home.models import Contacts, Home

class HomePage(ListView):
    model = Home
    context_object_name = 'Home'
    template_name = 'home/index.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Contact'] = Contacts.objects.all().filter(is_active=True)
        context['title'] = 'Главная'
        return context
    
    def get_queryset(self):
        return Home.objects.get(is_active=True)