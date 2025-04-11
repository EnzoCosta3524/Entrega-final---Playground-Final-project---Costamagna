from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('sobre/mi', views.about_me, name='about_me'),
    path('registrar', views.register, name='register'),
    path('lista/de/peliculas/', views.movies, name='movies'),
    path('crear/pelicula/', views.create_movies, name='create_movies'),
    path('pelicula/<int:id>', views.read_movies, name='read_movies'),
    path('actualizar/pelicula/<int:id>', views.update_movies, name='update_movies'),
    path('eliminar/pelicula/<int:id>', views.delete_movies, name='delete_movies')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
