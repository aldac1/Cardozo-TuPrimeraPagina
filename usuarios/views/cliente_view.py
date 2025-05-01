from django.views.generic import CreateView, UpdateView, DetailView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from usuarios.models.cliente import Cliente
from usuarios.forms.formulario_cliente import RegistroUsuarioForm, ClienteForm

class RegistroView(CreateView):
    template_name = 'registro.html'
    form_class = RegistroUsuarioForm
    success_url = reverse_lazy('login')


class CustomLoginView(LoginView):
    template_name = 'login.html'
    
    def get_success_url(self):
        return reverse_lazy('home')


class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('home')


class PerfilDetalleView(LoginRequiredMixin, DetailView):
    template_name = 'perfil_detalle.html'
    model = Cliente
    context_object_name = 'cliente'

    def get_object(self):
        cliente, created = Cliente.objects.get_or_create(user=self.request.user)
        return cliente



class PerfilClienteEditView(LoginRequiredMixin, UpdateView):
    template_name = 'perfil_editar.html'
    form_class = ClienteForm
    success_url = reverse_lazy('perfil')

    def get_object(self):
        return self.request.user.cliente