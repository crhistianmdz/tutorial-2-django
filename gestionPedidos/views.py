from gestionPedidos.admin import ArticulosAdmin
from django import http
from django.http import response
from django.shortcuts import render
from django.http import HttpResponse
from gestionPedidos.models import articulos
# Create your views here.


def busqueda_productos(request):
    return render(request,"busqueda_productos.html")

def buscar(request):
    if request.GET['prd']:
        #mensaje="articulos buscados: %r" %request.GET["prd"]
        producto=request.GET['prd']
        articulo=articulos.objects.filter(nombre__icontains=producto)
        return render(request, 'resultado_busqueda.html',{'articulos':articulo,'query':producto})
    else:
        mensaje='no ha introducido nada'



    
    return HttpResponse(mensaje)