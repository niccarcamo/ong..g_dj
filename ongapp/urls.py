from django.urls import path
from  . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('', views.index, name='index'),
    path('html/ClassicGames.html', views.classicgames, name='classicgames'),
    path('html/ClassicGames2.html', views.classicgames2, name='classicgames2'),
    path('html/Contactanos.html', views.contactanos, name='contactanos'),
    path('html/IniciarSesion.html', views.iniciarsesion, name='iniciarsesion'),
    path('html/NewGames.html', views.newgames, name='newgames'),
    path('html/NewGames2.html', views.newgames2, name='newgames2'),
    path('html/Nosotros.html', views.nosotros, name='nosotros'),
    path('html/Registrarse.html', views.registrarse, name='registrarse'),
    path('html/RetroGames.html', views.retrogames, name='retrogames'),
    path('html/RetroGames2.html', views.retrogames2, name='retrogames2'),
    

    
]