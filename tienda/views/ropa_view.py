from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
    DetailView,
)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from tienda.models.ropa import Ropa
from tienda.forms.formulario_ropa import RopaForm


class RopaListView(LoginRequiredMixin, ListView):
    model = Ropa
    template_name = "ropa_list.html"
    context_object_name = "ropas"


class RopaCreateView(LoginRequiredMixin, CreateView):
    model = Ropa
    template_name = "ropa_form.html"
    form_class = RopaForm
    success_url = reverse_lazy("ropa_list")


class RopaUpdateView(LoginRequiredMixin, UpdateView):
    model = Ropa
    form_class = RopaForm
    template_name = "ropa_form.html"
    success_url = reverse_lazy("ropa_list")



class RopaDeleteView(LoginRequiredMixin, DeleteView):
    model = Ropa
    template_name = "ropa_confirm_delete.html"
    success_url = reverse_lazy("ropa_list")


class RopaDetailView(LoginRequiredMixin, DetailView):
    model = Ropa
    template_name = "ropa_detail.html"
    context_object_name = "ropa"