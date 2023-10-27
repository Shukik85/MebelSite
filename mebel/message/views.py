from django.views.generic import DetailView, ListView
from message.models import Message


class MessagePage(ListView):
    model = Message
    paginate_by = 5
    context_object_name = "Works"
    template_name = "message/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Сообщения"
        return context
    
class ViewMessage(DetailView):
    model = Message
    template_name = "message/get_message.html"