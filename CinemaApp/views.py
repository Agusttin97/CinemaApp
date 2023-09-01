from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from .models import *
from .forms import *

# Create your views here.

def home(req):
    return render(req, 'home.html')

def cinema(req: HttpRequest): #Agregar cine
    
    if req.method == 'POST':
    
        myform = CinemaForm(req.POST)
        
        if myform.is_valid():
            print(myform.cleaned_data)
            data = myform.cleaned_data
            
            cinema = Cinema(name=data["name"], location=data["location"], capacity=data["capacity"])
            cinema.save()
            return render(req, 'home.html', {'msj': 'Cinema succesfully added'})
        else:
            return render(req, "home.html", {"msj": "Invalid form"})
        
    else:
        
        myform = CinemaForm()
        return render(req, "cinema.html", {"myform": myform})
    
def movie(req: HttpRequest): #Agregar pelicula
   
    if req.method == 'POST':
    
        myform = MovieForm(req.POST)
        
        if myform.is_valid():
            print(myform.cleaned_data)
            data = myform.cleaned_data
            
            movie = Movie(movie=data["movie"], genre=data["genre"], release=data["release"])
            movie.save()
            return render(req, 'home.html', {'msj': 'Movie succesfully added'})
        else:
            return render(req, "home.html", {"msj": "Invalid form"})
        
    else:
        
        myform = MovieForm()
        return render(req, "movie.html", {"myform": myform})

def user(req): #Agregar usuario
    
    if req.method == 'POST':
    
        myform = UserForm(req.POST)
        
        if myform.is_valid():
            print(myform.cleaned_data)
            data = myform.cleaned_data
            
            user = User(name=data["name"], surname=data["surname"], dni=data["dni"], email=data["email"])
            user.save()
            return render(req, 'home.html', {'msj': 'User succesfully added'})
        else:
            return render(req, "home.html", {"msj": "Invalid form"})
        
    else:
        
        myform = UserForm()
        return render(req, "user.html", {"myform": myform})

def searchMovie(req):
    return render(req, 'searchMovie.html')

def search(req): #Busqueda de pelicula
    
    if req.GET["movie"]: 
        movie = req.GET["movie"]
        res = Movie.objects.filter(movie__icontains=movie)
        return render(req, "searchResult.html", {"res": res}) #Contexto con nombre de pelicula y genero
          
    else:
        return HttpResponse('No escribiste ninguna pelicula')