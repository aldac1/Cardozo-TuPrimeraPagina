from django.urls import path
from tienda.views.home_view import home_view
from tienda.views.cliente_view import (
    cliente_list, cliente_create, cliente_update, cliente_delete
)
from tienda.views.ropa_view import (
    ropa_list, ropa_create, ropa_update, ropa_delete
)

urlpatterns = [
    path('', home_view, name='home'),

    # Cliente
    path('clientes/', cliente_list, name='cliente_list'),
    path('clientes/crear/', cliente_create, name='cliente_create'),
    path('clientes/<int:cliente_id>/editar/', cliente_update, name='cliente_update'),
    path('clientes/<int:cliente_id>/eliminar/', cliente_delete, name='cliente_delete'),

    # Ropa
    path('ropa/', ropa_list, name='ropa_list'),
    path('ropa/crear/', ropa_create, name='ropa_create'),
    path('ropa/<int:ropa_id>/editar/', ropa_update, name='ropa_update'),
    path('ropa/<int:ropa_id>/eliminar/', ropa_delete, name='ropa_delete'),
]
