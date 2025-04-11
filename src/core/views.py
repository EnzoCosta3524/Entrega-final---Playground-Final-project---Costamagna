from django.shortcuts import redirect, render
from .models import Pelicula
from .forms import PeliculaForm, RegisterForm

def index(request):
    obj = Pelicula.objects.all()
    nombre = {"obj":obj}
    return render (request, "core/index.html", context=nombre)

def about_me(request):
    return render (request, "core/about_me.html")

def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        form = RegisterForm()
    return render(response, "core/register.html", {"form":form})

# Lista de todas las películas
def movies(request):
    obj = Pelicula.objects.all()
    context = {'obj':obj}
    return render (request, "core/movies.html", context=context)

# Crea una nueva película
def create_movies(request):
    form = PeliculaForm()
    if request.method == 'POST':
        form = PeliculaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/lista/de/peliculas')
    contex = {'form': form}
    return render(request, 'core/movies_form.html', contex)

# Lee una película específica
def read_movies(request, id):
    obj = Pelicula.objects.get(id=id)
    context = {'obj': obj}
    return render(request, 'core/movies_read.html', context)

# Actualiza una película
def update_movies(request, id):
    obj = Pelicula.objects.get(id=id)
    form = PeliculaForm(instance=obj)
    if request.method == 'POST':
        form = PeliculaForm(request.POST, request.FILES, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'core/movies_upd.html', context)

# Elimina una película
def delete_movies(request, id):
    obj = Pelicula.objects.get(id=id)
    if request.method == 'POST':
        obj.delete()
        return redirect('/')
    context = {'obj': obj}
    return render(request, 'core/movies_del.html', context)