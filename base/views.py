from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from base.models import Client

class ClientCreateView(CreateView):
    model = Client
    template_name = 'form.html'
    fields = "__all__"
    success_url = reverse_lazy("homepage")


class ClientListView(ListView):
    template_name = "clients_list_view.html"
    model = Client


class ClientDetailView(DetailView):
    model = Client
    template_name = "clients_detail_view.html"


class ClientUpdateView(UpdateView):
    model = Client
    fields = "__all__"
    template_name = "form.html"
    success_url = reverse_lazy("homepage")


class ClientDeleteView(DeleteView):
    model = Client
    template_name = "clients_delete.html"
    success_url = reverse_lazy("homepage")