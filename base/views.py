from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView, FormView

from base.forms import ClientModelForm, AddressModelForm
from base.models import Client, Address
#testy do forms, walidacji i FormView
#zmienić na FormView i przypisać adres do klienta

class ClientModelFormView(FormView):
    template_name = "form.html"
    form_one = ClientModelForm
    form_two = AddressModelForm
    success_url = reverse_lazy("homepage")

    def form_valid(self, form):
        result = super().form_valid(form)
        form.save()
        return result


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



