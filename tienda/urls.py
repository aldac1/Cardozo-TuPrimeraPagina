from django.urls import path
from tienda.views.ropa_view import (
    RopaListView,
    RopaCreateView,
    RopaUpdateView,
    RopaDeleteView,
    RopaDetailView
)

urlpatterns = [
    path('', RopaListView.as_view(), name='ropa_list'),
    path('crear/', RopaCreateView.as_view(), name='ropa_create'),
    path('<int:pk>/editar/', RopaUpdateView.as_view(), name='ropa_update'),
    path('<int:pk>/eliminar/', RopaDeleteView.as_view(), name='ropa_delete'),
    path('<int:pk>/', RopaDetailView.as_view(), name='ropa_detail'),
]
