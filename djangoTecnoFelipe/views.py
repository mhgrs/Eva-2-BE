
from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto, Cliente
from .forms import ProductoForm, ClienteForm


""" inicio """
def index(request):
    return render(request, 'index.html')

def listaProductos(request):
    productos = Producto.objects.all()
    contexto = {'productos': productos}
    return render(request, 'djangoTecnoFelipe/listaProductos.html', contexto)


""" crear producto """
def crearProducto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listaProductos')
    else:
        form = ProductoForm()
    
    contexto = {
        'form': form,
        'tituloFormulario': 'Crear Nuevo Producto'
    }
    return render(request, 'djangoTecnoFelipe/formProducto.html', contexto)

def editarProducto(request, id):
    producto = get_object_or_404(Producto, idProducto=id)
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('listaProductos')
    else:
        form = ProductoForm(instance=producto)
    contexto = {
        'form': form,
        'tituloFormulario': f'Editar Producto'
    }
    return render(request, 'djangoTecnoFelipe/formProducto.html', contexto)

def eliminarProducto(request, id):
    producto = get_object_or_404(Producto, idProducto=id)
    producto.delete()
    return redirect('listaProductos')





def listaClientes(request):
    clientes = Cliente.objects.all()
    contexto = {'clientes': clientes}
   
    return render(request, 'djangoTecnoFelipe/listaClientes.html', contexto)

def crearCliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listaClientes')
    else:
        form = ClienteForm()
    
    contexto = {
        'form': form,
        'tituloFormulario': 'Crear Nuevo Cliente'
    }
    return render(request, 'djangoTecnoFelipe/formCliente.html', contexto)



def editarCliente(request, id):
    """ busca en la base de datos, si no existe muestra error """
    cliente = get_object_or_404(Cliente, idCliente=id) 
    
    if request.method == 'POST':
        """ crea la instancia, y le pasa request y los datos sin que cree uno nuevo """
        form = ClienteForm(request.POST, instance=cliente)
        """ valida """
        if form.is_valid():
            """ guarda en db """
            form.save()
            return redirect('listaClientes')
    else:
        form = ClienteForm(instance=cliente)
        
    contexto = {
        'form': form,
        'tituloFormulario': f'Editar Cliente'
    }
    return render(request, 'djangoTecnoFelipe/formCliente.html', contexto)



def eliminarCliente(request, id):
    cliente = get_object_or_404(Cliente, idCliente=id)
    cliente.delete()
    return redirect('listaClientes')