from django.http.response import Http404, HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.db import models
from django.urls import reverse
from django import forms

from .models import Articulos

# Create your views here.
def index(request):
    return render(request, 'stock\index.html')


def catalogo(request,):
    A = Articulos.objects.all()
    template = loader.get_template('stock\catalogo.html')
    context = {
        'A': A
    }
    return HttpResponse(template.render(context, request))


def movimientos(request):
    return render(request, 'stock\movimientos.html')

def det_art(request, art_id):
    try:
        art = Articulos.objects.get(pk=art_id)
    except Articulos.DoesNotExist:
            raise Http404("Articulo no exite")
    return render(request, 'stock/detalle_producto.html', {'a':art})


def suma(request, sumatoria):
    sumatoria = Articulos.objects.get(pk=sumatoria)
    var1 = request.POST['sumar']
    sumatoria.Cantidad += int(var1) 
    sumatoria.save()
    return HttpResponseRedirect(reverse('stock:catalogo',))

    
def resta(request, restatoria):
    restatoria = Articulos.objects.get(pk=restatoria)
    var1 = request.POST['restar']
    int(var1)
    restatoria.Cantidad -= int(var1) 
    restatoria.save()
    return HttpResponseRedirect(reverse('stock:catalogo',))
def articulo_nuevo(request):
    new_articulo = request.POST['Nombre_nuevo']
    new_descripcion = request.POST['Descripcion_nuevo']
    new_cantidad = request.POST['Cantidad_nueva']
    nregistro = Articulos( Articulo = new_articulo, Description = new_descripcion, Cantidad = new_cantidad)
    nregistro.save()
    return HttpResponseRedirect(reverse('stock:catalogo',))

