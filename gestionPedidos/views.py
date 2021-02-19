from gestionPedidos.admin import ArticulosAdmin
from django import http
from django.http import response
from django.shortcuts import render
from django.http import HttpResponse
from gestionPedidos.models import articulos
from django.core.mail import send_mail
from django.conf import settings
from gestionPedidos.forms import FormularioContacto
# Create your views here.


def busqueda_productos(request):
    return render(request,"busqueda_productos.html")

def buscar(request):
    if request.GET['prd']:
        #mensaje="articulos buscados: %r" %request.GET["prd"]
        producto=request.GET['prd']
        if len(producto)>20:
            mensaje='texto demasiado largo'
        else:
            articulo=articulos.objects.filter(nombre__icontains=producto)
            return render(request, 'resultado_busqueda.html',{'articulos':articulo,'query':producto})
    else:
        mensaje='no ha introducido nada'
    return HttpResponse(mensaje)

def contacto(request):

    if request.method=="POST":
        miFormulario=FormularioContacto(request.POST)
        if miFormulario.is_valid():
            infForm=miFormulario.cleaned_data
            send_mail(infForm['asunto'],infForm['mensaje'],infForm.get('email',' '), ['cristian648@hotmail.com'],)
            # subject=request.POST["asunto"]
            # message=request.POST['mensaje']+" "+ request.POST["email"]
            # email_from=settings.EMAIL_HOST_USER
            # recipient_list=["crhistianmendoza5@gmail.com"]
            # send_mail(subject, message,email_from,recipient_list)
            return render(request,'gracias.html')
    else:
        miFormulario=FormularioContacto()
        
#    return render(request,'contacto.html')
    return render(request,'formulario_contacto.html',{'form':miFormulario})