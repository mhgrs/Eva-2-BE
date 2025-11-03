# djangoTecnoFelipe/urls.py
from django.urls import path
from . import views

urlpatterns = [
    
    path('productos/', views.listaProductos, name='listaProductos'),
    path('productos/crear/', views.crearProducto, name='crearProducto'),
    path('productos/editar/<int:id>/', views.editarProducto, name='editarProducto'),
    path('productos/eliminar/<int:id>/', views.eliminarProducto, name='eliminarProducto'),

    
    path('clientes/', views.listaClientes, name='listaClientes'),
    path('clientes/crear/', views.crearCliente, name='crearCliente'),
    path('clientes/editar/<int:id>/', views.editarCliente, name='editarCliente'),
    path('clientes/eliminar/<int:id>/', views.eliminarCliente, name='eliminarCliente'),
]