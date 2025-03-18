from django.shortcuts import render
from .models import Cliente, Producto

def index(request):
    nombre = {"nombre":"Enzo"}
    return render (request, "core/index.html", context=nombre)

def clients(request):
    clientes = Cliente.objects.all()
    contexto = {"clientes":clientes}
    return render (request, "core/clients.html", context=contexto)

def products(request):
    productos = Producto.objects.all()
    contexto = {"productos":productos}
    return render (request, "core/products.html", context=contexto)