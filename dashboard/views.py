from pyexpat import model
from django.shortcuts import render, redirect
from dashboard.models import Contactos
from django.contrib import messages

# Create your views here.

def home(request):
    
    contactos = Contactos.objects.all()
    messages.success(request, "¡Contactos listados!")
    return render(request, "home.html", {"contactos" : contactos})

def registrar_contactos(request):
    
    if request.method == "POST":
        nombres = request.POST["contactos_nombres"]
        apellidos = request.POST["contactos_apellidos"]
        telefono = request.POST["contactos_telefono"]
        email = request.POST["contactos_email"]
    
        contactos = Contactos.objects.create(nombres = nombres, apellidos = apellidos, telefono = telefono, email = email)
        messages.success(request, "¡Contacto registrado!")
        return redirect("/")
    else:
        pass

def vista_registrar_contactos(request):

    return render(request, "crear_contactos.html")
    
def editar_contactos(request):
    
    if request.method == "POST":
        contactos_id = request.POST["contactos_id"]
        nombres = request.POST["contactos_nombres"]
        apellidos = request.POST["contactos_apellidos"]
        telefono = request.POST["contactos_telefono"]
        email = request.POST["contactos_email"]

        contactos = Contactos.objects.get(id = request.POST["contactos_id"])        

        contactos.id = contactos_id
        contactos.nombres = nombres
        contactos.apellidos = apellidos
        contactos.telefono = telefono
        contactos.email = email
        contactos.save()   
        
        messages.success(request, "¡Contacto actualizado!")
        
        return redirect('/')
    else:
        pass
    
def vista_editar_contactos(request, contactos_id):
    
    contactos = Contactos.objects.get(id = contactos_id)
    return render(request, "editar_contactos.html", {"contactos":contactos})

def eliminar_contactos(request, contactos_id):
    
    contactos = Contactos.objects.get(id = contactos_id)
    contactos.delete()
    
    messages.success(request, "¡Contacto eliminado!")
    return redirect("/")