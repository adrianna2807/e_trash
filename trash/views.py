from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView

from trash.models import Trash, EWaste, RWaste, HWaste, LSWaste


class TrashListView(LoginRequiredMixin, ListView):
    template_name = "list_view.html"
    model = Trash

class TrashCreateView(LoginRequiredMixin,CreateView):
    model = Trash
    fields = "__all__"
    template_name = "form.html"
    success_url = reverse_lazy("trash:ewastes-create-view")

class TrashDetailView(LoginRequiredMixin, DetailView):
    model = Trash
    template_name = "my_trashes.html"

class TrashUpdateView(LoginRequiredMixin, UpdateView):
    model = Trash
    fields = "__all__"
    template_name = "form.html"
    success_url = reverse_lazy("homepage")

class TrashDeleteView(LoginRequiredMixin, DeleteView):
    model = Trash
    template_name = "delete_trash.html"
    success_url = reverse_lazy("homepage")

class EWasteListView(LoginRequiredMixin, ListView):
    template_name = "list_view.html"
    model = EWaste

class EWasteCreateView(LoginRequiredMixin, CreateView):
    model = EWaste
    fields = "__all__"
    template_name = "form.html"
    success_url = reverse_lazy("homepage")

class EWasteDetailView(LoginRequiredMixin, DetailView):
    model = EWaste
    template_name = "my_ewastes.html"

class EWasteUpdateView(LoginRequiredMixin, UpdateView):
    model = EWaste
    fields = "__all__"
    template_name = "form.html"
    success_url = reverse_lazy("homepage")

class EWasteDeleteView(LoginRequiredMixin, DeleteView):
    model = EWaste
    template_name = "delete_ewaste.html"
    success_url = reverse_lazy("homepage")

class RWasteListView(LoginRequiredMixin, ListView):
    template_name = "list_view.html"
    model = RWaste

class RWasteCreateView(LoginRequiredMixin, CreateView):
    model = RWaste
    fields = "__all__"
    template_name = "form.html"
    success_url = reverse_lazy("homepage")

class RWasteDetailView(LoginRequiredMixin, DetailView):
    model = RWaste
    template_name = "my_rwastes.html"

class RWasteUpdateView(LoginRequiredMixin, UpdateView):
    model = RWaste
    fields = "__all__"
    template_name = "form.html"
    success_url = reverse_lazy("homepage")

class RWasteDeleteView(LoginRequiredMixin, DeleteView):
    model = RWaste
    template_name = "delete_rwaste.html"
    success_url = reverse_lazy("homepage")

class HWasteListView(LoginRequiredMixin, ListView):
    template_name = "list_view.html"
    model = HWaste

class HWasteCreateView(LoginRequiredMixin, CreateView):
    model = HWaste
    fields = "__all__"
    template_name = "form.html"
    success_url = reverse_lazy("homepage")

class HWasteDetailView(LoginRequiredMixin, DetailView):
    model = HWaste
    template_name = "my_hwastes.html"

class HWasteUpdateView(LoginRequiredMixin, UpdateView):
    model = HWaste
    fields = "__all__"
    template_name = "form.html"
    success_url = reverse_lazy("homepage")

class HWasteDeleteView(LoginRequiredMixin, DeleteView):
    model = HWaste
    template_name = "delete_hwaste.html"
    success_url = reverse_lazy("homepage")

class LSWasteListView(LoginRequiredMixin, ListView):
    template_name = "list_view.html"
    model = LSWaste

class LSWasteCreateView(LoginRequiredMixin, CreateView):
    model = LSWaste
    fields = "__all__"
    template_name = "form.html"
    success_url = reverse_lazy("homepage")

class LSWasteDetailView(LoginRequiredMixin, DetailView):
    model = LSWaste
    template_name = "my_lswastes.html"

class LSWasteUpdateView(LoginRequiredMixin, UpdateView):
    model = LSWaste
    fields = "__all__"
    template_name = "form.html"
    success_url = reverse_lazy("homepage")

class LSWasteDeleteView(LoginRequiredMixin, DeleteView):
    model = LSWaste
    template_name = "delete_lswaste.html"
    success_url = reverse_lazy("homepage")