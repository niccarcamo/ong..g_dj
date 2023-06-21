from django.shortcuts import render

# Create your views here.

def index(request):
    context={}
    return render(request, 'ongapp/index.html', context)

def classicgames(request):
    context={}
    return render(request, 'ongapp/html/ClassicGames.html', context)

def classicgames2(request):
    context={}
    return render(request, 'ongapp/html/ClassicGames2.html', context)

def contactanos(request):
    context={}
    return render(request, 'ongapp/html/Contactanos.html', context)

def iniciarsesion(request):
    context={}
    return render(request, 'ongapp/html/IniciarSesion.html', context)

def newgames(request):
    context={}
    return render(request, 'ongapp/html/NewGames.html', context)

def newgames2(request):
    context={}
    return render(request, 'ongapp/html/NewGames2.html', context)
    
def nosotros(request):
    context={}
    return render(request, 'ongapp/html/Nosotros.html', context)

def registrarse(request):
    context={}
    return render(request, 'ongapp/html/Registrarse.html', context)

def retrogames(request):
    context={}
    return render(request, 'ongapp/html/RetroGames.html', context)

def retrogames2(request):
    context={}
    return render(request, 'ongapp/html/RetroGames2.html', context)
    