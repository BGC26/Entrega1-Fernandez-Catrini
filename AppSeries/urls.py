from django.urls import path
from AppSeries.views import *

urlpatterns = [
    path('', home, name='home'),
    path('hbomax', hbomax, name='hbomax'),
    path('disneyplus', disneyplus, name='disneyplus'),
]