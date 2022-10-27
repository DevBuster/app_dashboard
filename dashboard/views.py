from pyexpat import model
from django.shortcuts import render, redirect
from dashboard.models import MuertesViolentas
from django.contrib import messages

# Create your views here.

def home(request):
    
    muertesViolentas = MuertesViolentas.objects.all()
    messages.success(request, "¡Registros Cargados!")
    return render(request, "home.html", {"muertesViolentas" : muertesViolentas})

def RegistrarMuertesViolentas(request):
    
    if request.method == "POST":
        tipoMuerte = request.POST["tipo-muerte"]
        numeroVictimas = request.POST["numeros-victimas"]
    
        muertesViolentas = MuertesViolentas.objects.create(tipoMuerte = tipoMuerte, numeroVictimas = numeroVictimas)
        messages.success(request, "¡Muerte Violenta registrada!")
        return redirect("/")
    else:
        pass

def VistaRegistrarMuertesViolentas(request):

    return render(request, "registrar_muertes_violentas.html")
    
# def editar_contactos(request):
    
#     if request.method == "POST":
#         contactos_id = request.POST["contactos_id"]
#         nombres = request.POST["contactos_nombres"]
#         apellidos = request.POST["contactos_apellidos"]
#         telefono = request.POST["contactos_telefono"]
#         email = request.POST["contactos_email"]

#         contactos = Contactos.objects.get(id = request.POST["contactos_id"])        

#         contactos.id = contactos_id
#         contactos.nombres = nombres
#         contactos.apellidos = apellidos
#         contactos.telefono = telefono
#         contactos.email = email
#         contactos.save()   
        
#         messages.success(request, "¡Contacto actualizado!")
        
#         return redirect('/')
#     else:
#         pass
    
# def vista_editar_contactos(request, contactos_id):
    
#     contactos = Contactos.objects.get(id = contactos_id)
#     return render(request, "editar_contactos.html", {"contactos":contactos})

# def eliminar_contactos(request, contactos_id):
    
#     contactos = Contactos.objects.get(id = contactos_id)
#     contactos.delete()
    
#     messages.success(request, "¡Contacto eliminado!")
#     return redirect("/")