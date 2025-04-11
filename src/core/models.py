from django.db import models

class Pais(models.Model):
    nombre = models.CharField(max_length=50)

    def  __str__(self):
        return self.nombre 

class Director(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    edad = models.PositiveSmallIntegerField()
    pais_de_origen = models.ForeignKey(Pais, on_delete=models.PROTECT, null=True, blank=True)

    def  __str__(self):
        return f"{self.nombre} {self.apellido} {self.pais_de_origen}"
    
class Pelicula(models.Model):
    nombre = models.CharField(max_length=150)
    descripcion = models.TextField(blank=True, null=True)
    puntaje = models.DecimalField(max_digits=10, decimal_places=0)
    duracion = models.DecimalField(max_digits=10, decimal_places=0)
    genero = models.CharField(max_length=150)
    año = models.PositiveSmallIntegerField(blank=True, null=True)
    director = models.ForeignKey(Director, on_delete=models.PROTECT, null=True, blank=True)
    poster = models.ImageField(default='boludo.jpg', blank=True, null=True)

    def __str__(self):
        return self.nombre