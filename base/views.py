from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView, FormView

from base.forms import ClientForm, AddressForm, RecyclerForm, OrderForm
from base.models import Client, Address, Recycler, Order


#testy do forms, walidacji i FormView
#zmienić na FormView i przypisać adres do klienta



def client_address_create(request):
    form = ClientForm(request.POST or None)
    form_2 = AddressForm(request.POST or None)
    if all([form.is_valid(), form_2.is_valid()]):
        first_name = form.cleaned_data["first_name"]
        last_name = form.cleaned_data["last_name"]
        email = form.cleaned_data["email"]
        phone = form.cleaned_data["phone"]
        zone = form.cleaned_data["zone"]
        street = form_2.cleaned_data["street"]
        city = form_2.cleaned_data["city"]
        postal_code = form_2.cleaned_data["postal_code"]
        Client.objects.create(first_name=first_name, last_name=last_name, email=email, phone=phone, zone=zone)
        Address.objects.create(street=street, city=city, postal_code=postal_code)
        return HttpResponse("IT WORKED")
    return render(
        request,
        template_name="client_address.html",
        context={"form": form,
                     "form_2": form_2})


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

# WIDOKI RECYCLER

class RecyclerFormView(FormView):
    template_name = "form.html"
    form_class = RecyclerForm
    success_url = reverse_lazy("homepage")

    def form_valid(self, form):
        result = super().form_valid(form)
        name = form.cleaned_data["name"]
        street = form.cleaned_data["street"]
        city = form.cleaned_data["city"]
        postal_code = form.cleaned_data["postal_code"]
        nip = form.cleaned_data["nip"]
        available_days = form.cleaned_data["available_days"]
        capacity = form.cleaned_data["capacity"]
        type = form.cleaned_data["type"]
        zone = form.cleaned_data["zone"]
        Recycler.objects.create(
            name=name,
            street=street,
            city=city,
            postal_code=postal_code,
            nip=nip,
            available_days=available_days,
            capacity=capacity,
            type=type,
            zone=zone
        )
        return result

    def form_invalid(self, form):
        return super().form_invalid(form)

# WIDOKI ORDERS

class OrderFormView(FormView):
    template_name = "form.html"
    form_class = OrderForm
    success_url = reverse_lazy("homepage")

    def form_valid(self, form):
        result = super().form_valid(form)
        order_number = form.cleaned_data["order_number"]
        order_day = form.cleaned_data["order_day"]
        order_time = form.cleaned_data["order_time"]
        order_date = form.cleaned_data["order_date"]
        zone = form.cleaned_data["zone"]
        address = form.cleaned_data["address"]
        trash_type = form.cleaned_data["trash_type"]
        Order.objects.create(
            order_number=order_number,
            order_day=order_day,
            order_time=order_time,
            order_date=order_date,
            zone=zone,
            address=address,
            trash_type=trash_type,
        )
        return result

    def form_invalid(self, form):
        return super().form_invalid(form)