from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from AppSeries.forms import *

# Create your views here.

def home(request):
    return render(request, "home.html")

def netflix(request):
    serienetflix1 = Netflix(photo=f"https://statics.forbesargentina.com/2022/05/628658a73c567.jpg", qualification=8.7, title="Stranger Things")
    serienetflix2 = Netflix(photo=f"https://es.web.img2.acsta.net/newsv7/21/05/31/15/47/4895222.jpg", qualification=8.9, title="Better Call Saul")
    serienetflix3 = Netflix(photo=f"https://imagenes.elpais.com/resizer/VSa-Lw4aYZ8Ss2d3DqWn-c4OTOo=/1960x1103/ep01.epimg.net/elpais/imagenes/2019/10/03/icon/1570108033_716305_1570517193_noticia_fotograma.jpg", qualification=8.8, title="Peaky Blinders")
    serienetflix4 = Netflix(photo=f"https://img.europapress.es/fotoweb/fotonoticia_20220428182149_1200.jpg", qualification=8.5, title="Ozark")
    serienetflix1.save()
    serienetflix2.save()
    serienetflix3.save()
    serienetflix4.save()
    listanetflix = [serienetflix1, serienetflix2, serienetflix3, serienetflix4]
    return render(request, "netflix.html", {'listanetflix':listanetflix})

def primevideo(request):
    serieprime1 = Prime(photo=f"https://m.media-amazon.com/images/M/MV5BOTYwN2RiODItNjZhZC00NjlmLWIxYjctNTQ5NjEyZDlhYzU0XkEyXkFqcGdeQXNoYW5nZWxs._V1_QL75_UX500_CR0,0,500,281_.jpg", qualification=8, title="The Terminal List")
    serieprime2 = Prime(photo=f"https://cdn.mos.cms.futurecdn.net/nN8c6fA94tq3ZVNJCajMaS.jpg", qualification=6.7, title="The Lord of the Rings: The Rings of Power")
    serieprime3 = Prime(photo=f"https://media.ambito.com/p/98ce50b9810e18e1bab9d98b530c8e2e/adjuntos/239/imagenes/039/860/0039860427/the-boys-3webp.png", qualification=8.7, title="The Boys")
    serieprime4 = Prime(photo=f"https://rotaprincipal.com.br/wp-content/uploads/2018/12/this-is-us-1.jpg", qualification=8.7, title="This Is Us")
    serieprime1.save()
    serieprime2.save()
    serieprime3.save()
    serieprime4.save()
    listaprime = [serieprime1, serieprime2, serieprime3, serieprime4]
    return render(request, "primevideo.html", {'listaprime':listaprime})

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

def netflixForm(request):
    if request.method == "POST":
        form = NetflixForm(request.POST)
        print(form)
        if form.is_valid():
            informacion = form.cleaned_data
            print(informacion)
            title = informacion["title"]
            qualification = informacion["qualification"]
            photo = informacion["photo"]
            netflix = Netflix(title=title, qualification=qualification, photo=photo)
            netflix.save()
            return render (request, "home.html")

    else:
        formulario = NetflixForm()
        return render(request, "netflixForm.html", {"formulario":formulario})


def primeForm(request):
    if request.method == "POST":
        form = PrimeForm(request.POST)
        print(form)
        if form.is_valid():
            informacion = form.cleaned_data
            print(informacion)
            title = informacion["title"]
            qualification = informacion["qualification"]
            photo = informacion["photo"]
            prime = Prime(title=title, qualification=qualification, photo=photo)
            prime.save()
            return render (request, "home.html")

    else:
        formulario = PrimeForm()
        return render(request, "primeForm.html", {"formulario":formulario})
        
def hboForm(request):
    if request.method == "POST":
        form = HBOForm(request.POST)
        print(form)
        if form.is_valid():
            informacion = form.cleaned_data
            print(informacion)
            title = informacion["title"]
            qualification = informacion["qualification"]
            photo = informacion["photo"]
            hbo = HBO(title=title, qualification=qualification, photo=photo)
            hbo.save()
            return render (request, "home.html")

    else:
        formulario = HBOForm()
        return render(request, "hboForm.html", {"formulario":formulario})

def disneyForm(request):
    if request.method == "POST":
        form = DisneyForm(request.POST)
        print(form)
        if form.is_valid():
            informacion = form.cleaned_data
            print(informacion)
            title = informacion["title"]
            qualification = informacion["qualification"]
            photo = informacion["photo"]
            disney = Disney(title=title, qualification=qualification, photo=photo)
            disney.save()
            return render (request, "home.html")

    else:
        formulario = DisneyForm()
        return render(request, "disneyForm.html", {"formulario":formulario})

def buscarSerieNetflix(request):
    if request.GET["title"]:
        title = request.GET["title"]
        netflixseries = Netflix.objects.filter(title__icontains = title)
        return render(request, "resultadoNetflix.html", {"netflixseries": netflixseries, "title": title})

    else:
        respuesta = "No has enviado datos"
    
    return HttpResponse(respuesta)

def busquedaNetflix(request):
    return render(request, "busquedaNetflix.html")

def buscarSeriePrime(request):
    if request.GET["title"]:
        title = request.GET["title"]
        primeseries = Prime.objects.filter(title__icontains = title)
        return render(request, "resultadoPrime.html", {"primeseries": primeseries, "title": title})

    else:
        respuesta = "No has enviado datos"
    
    return HttpResponse(respuesta)

def busquedaPrime(request):
    return render(request, "busquedaPrime.html")

def buscarSerieHBO(request):
    if request.GET["title"]:
        title = request.GET["title"]
        hboseries = HBO.objects.filter(title__icontains = title)
        return render(request, "resultadoHBO.html", {"hboseries": hboseries, "title": title})

    else:
        respuesta = "No has enviado datos"
    
    return HttpResponse(respuesta)


def busquedaHBO(request):
    return render(request, "busquedaHBO.html")


def buscarSerieDisney(request):
    if request.GET["title"]:
        title = request.GET["title"]
        disneyseries = Disney.objects.filter(title__icontains = title)
        return render(request, "resultadoDisney.html", {"disneyseries": disneyseries, "title": title})

    else:
        respuesta = "No has enviado datos"
    
    return HttpResponse(respuesta)


def busquedaDisney(request):
    return render(request, "busquedaDisney.html")