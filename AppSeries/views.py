from django.shortcuts import render
from .models import *

# Create your views here.

def home(request):
    return render(request, "home.html")

def hbomax(request):
    seriehbo1 = HBO(photo=f"https://media.glamour.mx/photos/62df41dcc780ec35bf4be112/16:9/w_2560%2Cc_limit/House%2520of%2520the%2520Dragon.jpg", qualification=8.8, title="House of the Dragon")
    seriehbo2 = HBO(photo=f"https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/succession-hbo-serie-analisis-10-1534539573.jpg", qualification=8.8, title="Succesion")
    seriehbo3 = HBO(photo=f"https://www.otroscines.com/images/fotos/the-flight-attendant-critica-800.jpeg", qualification=7.1, title="The Flight Attendant")
    seriehbo4 = HBO(photo=f"https://i.blogs.es/ac96df/temporada-dos/840_560.jpg", qualification=8.5, title="Westworld")
    seriehbo1.save()
    seriehbo2.save()
    seriehbo3.save()
    seriehbo4.save()
    listahbo = [seriehbo1, seriehbo2, seriehbo3, seriehbo4]
    return render(request, "hbomax.html", {'listahbo':listahbo})

def disneyplus(request):
    seriedisney1 = Disney(photo=f"https://filmparadiset.se/wp-content/uploads/2022/07/She-Hulk-Attorney-at-Law-Featured.jpg", qualification=5.1, title="She-Hulk: Attorney at Law")
    seriedisney2 = Disney(photo=f"https://media.gq.com.mx/photos/6272aa451e7e8a4eaa1edcad/16:9/w_2560%2Cc_limit/moon%2520knight.jpg", qualification=7.3, title="Moon Knight")
    seriedisney3 = Disney(photo=f"https://images6.alphacoders.com/124/1245209.jpg", qualification=6.2, title="Ms. Marvel")
    seriedisney4 = Disney(photo=f"https://cinematicos.net/wp-content/uploads/b9bd02f8-0842-4a77-9a3f-af1b5a28c3f9-obi-wan-header.jpg", qualification=7.1, title="Obi-Wan Kenobi")
    seriedisney1.save()
    seriedisney2.save()
    seriedisney3.save()
    seriedisney4.save()
    listadisney = [seriedisney1, seriedisney2, seriedisney3, seriedisney4]
    return render(request, "disneyplus.html", {'listadisney':listadisney})