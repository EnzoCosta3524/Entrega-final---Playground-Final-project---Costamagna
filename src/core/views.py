from django.shortcuts import redirect, render
from django.contrib.auth import login,logout
from .models import Pelicula
from .forms import PeliculaForm, RegisterForm, LoginForm

def index(request):
    search = request.GET.get("search")
    if search:
        obj = Pelicula.objects.filter(nombre__istartswith=search)
    else:
        obj = Pelicula.objects.all()
    nombre = {"obj":obj}
    return render (request, "core/index.html", context=nombre)

def about_me(request):
    return render (request, "core/about_me.html")

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        form = RegisterForm()
    return render(request, "core/register.html", {"form":form})

def log_in(request):
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect("/")
    else:
        form = LoginForm()
    context = {'form': form}
    return render(request, "core/login.html", context=context)

def log_out(request):
    if request.method == "POST":
        logout(request)
        return redirect("/")


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