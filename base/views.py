from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, FormView

from base.forms import ClientForm, AddressForm, RecyclerForm, OrderForm
from base.models import Client, Address, Recycler


# testy do forms, walidacji i FormView


# WIDOKI CLIENT

@login_required
def client_address_create(request):
    form = ClientForm(request.POST or None)
    form_2 = AddressForm(request.POST or None)
    if all([form.is_valid(), form_2.is_valid()]):
        first_name = form.cleaned_data["first_name"]
        last_name = form.cleaned_data["last_name"]
        email = form.cleaned_data["email"]
        phone = form.cleaned_data["phone"]
        strefa = form.cleaned_data["strefa"]
        street = form_2.cleaned_data["street"]
        city = form_2.cleaned_data["city"]
        postal_code = form_2.cleaned_data["postal_code"]
        client = Client.objects.create(user=request.user, first_name=first_name, last_name=last_name, email=email,
                                       phone=phone, strefa=strefa)
        Address.objects.create(user=request.user, street=street, city=city, postal_code=postal_code)
        return redirect("/base/clients-detail-view/")
    return render(
        request,
        template_name="client_address.html",
        context={"form": form,
                 "form_2": form_2})


class CurrentUserMixin(object):
    model = Client

    def get_object(self, *args, **kwargs):
        return self.request.user.client
        # try:
        #     obj = super(CurrentUserMixin, self).get_object(*args, **kwargs)
        # except AttributeError:
        #     obj = self.request.user.client

        # return obj


class ClientListView(LoginRequiredMixin, ListView):
    template_name = "clients_list_view.html"
    model = Client


class ClientDetailView(LoginRequiredMixin, CurrentUserMixin, DetailView):
    model = Client
    template_name = "clients_detail_view.html"


class ClientUpdateView(LoginRequiredMixin, UpdateView):
    model = Client
    fields = "__all__"
    template_name = "form.html"
    success_url = reverse_lazy("homepage")


class ClientDeleteView(LoginRequiredMixin, DeleteView):
    model = Client
    template_name = "clients_delete.html"
    success_url = reverse_lazy("homepage")


# WIDOKI RECYCLER

class RecyclerFormView(LoginRequiredMixin, FormView):
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
            user=self.request.user,
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

class OrderFormView(LoginRequiredMixin, FormView):
    template_name = "order_form.html"
    form_class = OrderForm
    success_url = reverse_lazy("homepage")

    # def form_valid(self, form):
    #     result = super().form_valid(form)
    #     order_number = form.cleaned_data["order_number"]
    #     order_day = form.cleaned_data["order_day"]
    #     order_time = form.cleaned_data["order_time"]
    #     # order_date = form.cleaned_data["order_date"]
    #     zone = form.cleaned_data["zone"]
    #     address = form.cleaned_data["address"]
    #     trash_type = form.cleaned_data["trash_type"]
    #     Order.objects.create(
    #         order_number=order_number,
    #         order_day=order_day,
    #         order_time=order_time,
    #         # order_date=order_date,
    #         zone=zone,
    #         address=address,
    #         trash_type=trash_type,
    #     )
    #     return result
    #
    # def form_invalid(self, form):
    #     return super().form_invalid(form)


@login_required
def order_user(request):
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            form.instance.client = request.user.client
            form.save()
            trash = form.cleaned_data["trash_type"]
            if trash == "Odpad Elektryczny":
                # return redirect("/trash/ewastes-create-view/")
                return redirect("/trash/orders-ewaste/")
            if trash == "Odpady z Recyklingu":
                # return redirect("/trash/rwastes-create-view/")
                return redirect("/trash/orders-rwaste/")
            if trash == "Niebezpieczne Odpady":
                # return redirect("/trash/hwastes-create-view/")
                return redirect("/trash/orders-hwaste/")
            if trash == "Wielkogabarytowe Odpady":
                # return redirect("/trash/lswastes-create-view/")
                return redirect("/trash/orders-lswaste/")

    else:
        form = OrderForm
    return render(request, 'form.html', {"form": form})
