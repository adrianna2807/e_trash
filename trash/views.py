from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView

from trash.models import Trash, EWaste, RWaste, HWaste, LSWaste


class TrashListView(ListView):
    template_name = "list_view.html"
    model = Trash

class TrashCreateView(CreateView):
    model = Trash
    fields = "__all__"
    template_name = "form.html"
    success_url = reverse_lazy("homepage")

class TrashDetailView(DetailView):
    model = Trash
    template_name = "my_trashes.html"

class TrashUpdateView(UpdateView):
    model = Trash
    fields = "__all__"
    template_name = "form.html"
    success_url = reverse_lazy("homepage")

class TrashDeleteView(DeleteView):
    model = Trash
    template_name = "delete_trash.html"
    success_url = reverse_lazy("homepage")

class EWasteListView(ListView):
    template_name = "list_view.html"
    model = EWaste

class EWasteCreateView(CreateView):
    model = EWaste
    fields = "__all__"
    template_name = "form.html"
    success_url = reverse_lazy("homepage")

class EWasteDetailView(DetailView):
    model = EWaste
    template_name = "my_ewastes.html"

class EWasteUpdateView(UpdateView):
    model = EWaste
    fields = "__all__"
    template_name = "form.html"
    success_url = reverse_lazy("homepage")

class EWasteDeleteView(DeleteView):
    model = EWaste
    template_name = "delete_ewaste.html"
    success_url = reverse_lazy("homepage")

class RWasteListView(ListView):
    template_name = "list_view.html"
    model = RWaste

class RWasteCreateView(CreateView):
    model = RWaste
    fields = "__all__"
    template_name = "form.html"
    success_url = reverse_lazy("homepage")

class RWasteDetailView(DetailView):
    model = RWaste
    template_name = "my_rwastes.html"

class RWasteUpdateView(UpdateView):
    model = RWaste
    fields = "__all__"
    template_name = "form.html"
    success_url = reverse_lazy("homepage")

class RWasteDeleteView(DeleteView):
    model = RWaste
    template_name = "delete_rwaste.html"
    success_url = reverse_lazy("homepage")

class HWasteListView(ListView):
    template_name = "list_view.html"
    model = HWaste

class HWasteCreateView(CreateView):
    model = HWaste
    fields = "__all__"
    template_name = "form.html"
    success_url = reverse_lazy("homepage")

class HWasteDetailView(DetailView):
    model = HWaste
    template_name = "my_hwastes.html"

class HWasteUpdateView(UpdateView):
    model = HWaste
    fields = "__all__"
    template_name = "form.html"
    success_url = reverse_lazy("homepage")

class HWasteDeleteView(DeleteView):
    model = HWaste
    template_name = "delete_hwaste.html"
    success_url = reverse_lazy("homepage")

class LSWasteListView(ListView):
    template_name = "list_view.html"
    model = LSWaste

class LSWasteCreateView(CreateView):
    model = LSWaste
    fields = "__all__"
    template_name = "form.html"
    success_url = reverse_lazy("homepage")

class LSWasteDetailView(DetailView):
    model = LSWaste
    template_name = "my_lswastes.html"

class LSWasteUpdateView(UpdateView):
    model = LSWaste
    fields = "__all__"
    template_name = "form.html"
    success_url = reverse_lazy("homepage")

class LSWasteDeleteView(DeleteView):
    model = LSWaste
    template_name = "delete_lswaste.html"
    success_url = reverse_lazy("homepage")