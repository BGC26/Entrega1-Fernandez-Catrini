from django.urls import path
from AppSeries.views import *

urlpatterns = [
    path('', home, name='home'),
    path('netflix', netflix, name='netflix'),
    path('primevideo', primevideo, name='primevideo'),
    path('netflixForm', netflixForm, name='netflixForm'),
    path('primeForm', primeForm, name='primeForm'),
    path('hbomax', hbomax, name='hbomax'),
    path('disneyplus', disneyplus, name='disneyplus'),
    path('hboForm', hboForm, name='hboForm'),
    path('disneyForm', disneyForm, name='disneyForm'),
    path('busquedaNetflix', busquedaNetflix, name='busquedaNetflix'),
    path('buscarSerieNetflix/', buscarSerieNetflix),
    path('busquedaPrime', busquedaPrime, name='busquedaPrime'),
    path('buscarSeriePrime/', buscarSeriePrime),
    path('busquedaHBO', busquedaHBO, name='busquedaHBO'),
    path('buscarSerieHBO/', buscarSerieHBO),
    path('busquedaDisney', busquedaDisney, name='busquedaDisney'),
    path('buscarSerieDisney/', buscarSerieDisney),
]