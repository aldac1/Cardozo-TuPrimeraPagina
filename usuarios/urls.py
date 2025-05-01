from django.urls import path
from usuarios.views.cliente_view import (
    RegistroView,
    CustomLoginView,
    CustomLogoutView,
    PerfilDetalleView,
    PerfilClienteEditView
)
urlpatterns = [
    path('registro/', RegistroView.as_view(), name='registro'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('perfil/', PerfilDetalleView.as_view(), name='perfil'),
    path('perfil/editar/', PerfilClienteEditView.as_view(), name='perfil_editar'),
]
