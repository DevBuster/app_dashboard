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
    
    muertesViolenyas = MuertesViolentas.objects.get(id = muertesViolentas_id)
    muertesViolenyas.delete()
    
    messages.success(request, "Muerte Violenta eliminada!")
    return redirect("/")