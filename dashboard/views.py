from pyexpat import model
from django.shortcuts import render, redirect
from dashboard.models import MuertesViolentas
from dashboard.models import MuertesAccidentes
from dashboard.models import MuertesAccidentales
from dashboard.models import MuertesHomicidios
from django.contrib import messages

# Create your views here.

def home(request):
    
    muertesViolentas = MuertesViolentas.objects.all()
    muertesAccidentes = MuertesAccidentes.objects.all()
    muertesAccidentales = MuertesAccidentales.objects.all()
    muertesHomicidios = MuertesHomicidios.objects.all()
    messages.success(request, "¡Registros Cargados!")
    return render(request, "home.html", {"muertesViolentas" : muertesViolentas, 
                                         "muertesAccidentes" : muertesAccidentes,
                                        "muertesAccidentales" : muertesAccidentales,
                                        "muertesHomicidios" : muertesHomicidios})

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
#----------------------------------------------------------------------------------------------------

def RegistrarMuertesAccidentales(request):
    
    if request.method == "POST":
        tipoAccidente = request.POST["tipo_accidente"]
        numeroVictimas = request.POST["numeros_victimas"]
    
        muertesAccidentales = MuertesAccidentales.objects.create(tipoAccidente = tipoAccidente, numeroVictimas = numeroVictimas)
        messages.success(request, "¡Muerte accidentales registrada!")
        return redirect("/")
    else:
        pass

def VistaRegistrarMuertesAccidentales(request):

    return render(request, "crear_muertes_accidentales.html")
    
def EditarMuertesAccidentales(request):
    
    if request.method == "POST":
        muertesAccidentales_id =  request.POST["muertesAccidentales_id"]
        tipoAccidente = request.POST["tipo_accidente"]
        numeroVictimas = request.POST["numero_victimas"]

        muertesAccidentales = MuertesAccidentales.objects.get(id = request.POST["muertesAccidentales_id"])        

        muertesAccidentales.id = muertesAccidentales_id
        muertesAccidentales.tipoVehiculo = tipoAccidente
        muertesAccidentales.numeroVictimas = numeroVictimas
        
        muertesAccidentales.save()   
        
        messages.success(request, "Muerte accidentales Actualizada!")
        
        return redirect('/')
    else:
        pass
    
def VistaEditarMuertesAccidentales(request, muertesAccidentales_id):
    
    muertesAccidentales = MuertesAccidentales.objects.get(id = muertesAccidentales_id)
    return render(request, "editar_muertes_accidentales.html", {"muertesAccidentales" : muertesAccidentales})

def EliminarMuertesAccidentes(request, muertesAccidentales_id):
    
    muertesAccidentales = MuertesAccidentales.objects.get(id = muertesAccidentales_id)
    muertesAccidentales.delete()
    
    messages.success(request, "Muerte accidentales eliminada!")
    return redirect("/")
#----------------------------------------------------------------------------------------------------

def RegistrarMuertesHomicidios(request):
    
    if request.method == "POST":
        tipoHomicidio = request.POST["tipo_homicidio"]
        numeroVictimas = request.POST["numeros_victimas"]
    
        muertesHomicidio = MuertesHomicidios.objects.create(tipoHomicidio = tipoHomicidio, numeroVictimas = numeroVictimas)
        messages.success(request, "¡Muerte homicidio registrada!")
        return redirect("/")
    else:
        pass

def VistaRegistrarMuertesHomicidios(request):

    return render(request, "crear_muertes_homicidio.html")
    
def EditarMuertesHomicidios(request):
    
    if request.method == "POST":
        muertesHomicidio_id =  request.POST["muertesHomicidio_id"]
        tipoHomicidio = request.POST["tipo_homicidio"]
        numeroVictimas = request.POST["numero_victimas"]

        muertesHomicidio = MuertesHomicidios.objects.get(id = request.POST["muertesHomicidio_id"])        

        muertesHomicidio.id = muertesHomicidio_id
        muertesHomicidio.tipoHomicidio = tipoHomicidio
        muertesHomicidio.numeroVictimas = numeroVictimas
        
        muertesHomicidio.save()   
        
        messages.success(request, "Muerte homicidio Actualizada!")
        
        return redirect('/')
    else:
        pass
    
def VistaEditarMuertesHomidicios(request, muertesHomicidio_id):
    
    muertesHomicidio = MuertesHomicidios.objects.get(id = muertesHomicidio_id)
    return render(request, "editar_muertes_homicidio.html", {"muertesHomicidio" : muertesHomicidio})

def EliminarMuertesHomidicios(request, muertesHomicidio_id):
    
    muertesHomicidio = MuertesHomicidios.objects.get(id = muertesHomicidio_id)
    muertesHomicidio.delete()
    
    messages.success(request, "Muerte homicidio eliminada!")
    return redirect("/")