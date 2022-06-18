from django.urls import reverse_lazy
from django.views.generic import CreateView
from base.models import Client

class ClientCreateView(CreateView):
    model = Client
    template_name = 'form.html'
    fields = "__all__"
    #success_url = reverse_lazy("polls:polls-list-view")
