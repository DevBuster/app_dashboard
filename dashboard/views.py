from pyexpat import model
from django.shortcuts import render, redirect
from dashboard.models import MuertesViolentas
from dashboard.models import MuertesAccidentes
from django.contrib import messages

# Create your views here.

def home(request):
    
    muertesViolentas = MuertesViolentas.objects.all()
    muertesAccidentes = MuertesAccidentes.objects.all()
    messages.success(request, "¡Registros Cargados!")
    return render(request, "home.html", {"muertesViolentas" : muertesViolentas, "muertesAccidentes" : muertesAccidentes})

def RegistrarMuertesViolentas(request):
    
    if request.method == "POST":
        tipoMuerte = request.POST["tipo_muerte"]
        numeroVictimas = request.POST["numeros_victimas"]
    
        muertesViolentas = MuertesViolentas.objects.create(tipoMuerte = tipoMuerte, numeroVictimas = numeroVictimas)
        messages.success(request, "¡Muerte Violenta registrada!")
        return redirect("/")
    else:
        pass

def VistaRegistrarMuertesViolentas(request):

    return render(request, "registrar_muertes_violentas.html")
    
def EditarMuertesViolentas(request):
    
    if request.method == "POST":
        muertesViolentas_id =  request.POST["muertesViolentas_id"]
        tipoMuerte = request.POST["tipo_muerte"]
        numeroVictimas = request.POST["numero_victimas"]

        muertesViolentas = MuertesViolentas.objects.get(id = request.POST["muertesViolentas_id"])        

        muertesViolentas.id = muertesViolentas_id
        muertesViolentas.tipoMuerte = tipoMuerte
        muertesViolentas.numeroVictimas = numeroVictimas
        
        muertesViolentas.save()   
        
        messages.success(request, "Muerte Violenta Actualizada!")
        
        return redirect('/')
    else:
        pass
    
def VistaEditarMuertesViolentas(request, muertesViolentas_id):
    
    muertesViolentas = MuertesViolentas.objects.get(id = muertesViolentas_id)
    return render(request, "editar_muertes_violentas.html", {"muertesViolentas" : muertesViolentas})

def EliminarMuertesViolentas(request, muertesViolentas_id):
    
    muertesViolentas = MuertesViolentas.objects.get(id = muertesViolentas_id)
    muertesViolentas.delete()
    
    messages.success(request, "Muerte Violenta eliminada!")
    return redirect("/")
#----------------------------------------------------------------------------------------------------

def RegistrarMuertesAccidentes(request):
    
    if request.method == "POST":
        tipoVehiculo = request.POST["tipo_vehiculo"]
        numeroVictimas = request.POST["numeros_victimas"]
    
        muertesAccidentes = MuertesAccidentes.objects.create(tipoVehiculo = tipoVehiculo, numeroVictimas = numeroVictimas)
        messages.success(request, "¡Muerte accidente registrada!")
        return redirect("/")
    else:
        pass

def VistaRegistrarMuertesAccidentes(request):

    return render(request, "crear_muertes_accidentes.html")
    
def EditarMuertesAccidentes(request):
    
    if request.method == "POST":
        muertesAccidentes_id =  request.POST["muertesAccidentes_id"]
        tipoVehiculo = request.POST["tipo_vehiculo"]
        numeroVictimas = request.POST["numero_victimas"]

        muertesAccidentes = MuertesAccidentes.objects.get(id = request.POST["muertesAccidentes_id"])        

        muertesAccidentes.id = muertesAccidentes_id
        muertesAccidentes.tipoVehiculo = tipoVehiculo
        muertesAccidentes.numeroVictimas = numeroVictimas
        
        muertesAccidentes.save()   
        
        messages.success(request, "Muerte accidente Actualizada!")
        
        return redirect('/')
    else:
        pass
    
def VistaEditarMuertesAccidentes(request, muertesAccidentes_id):
    
    muertesAccidentes = MuertesAccidentes.objects.get(id = muertesAccidentes_id)
    return render(request, "editar_muertes_accidentes.html", {"muertesAccidentes" : muertesAccidentes})

def EliminarMuertesAccidentes(request, muertesAccidentes_id):
    
    muertesAccidentes = MuertesAccidentes.objects.get(id = muertesAccidentes_id)
    muertesAccidentes.delete()
    
    messages.success(request, "Muerte accidente eliminada!")
    return redirect("/")