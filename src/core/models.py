from django.db import models

class Pais (models.Model):
    nombre = models.CharField(max_length=50)

    def  __str__(self):
        return self.nombre 

class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    cliente_pais = models.ForeignKey(Pais, on_delete=models.PROTECT, null=True, blank=True)

    def  __str__(self):
        return f"{self.nombre} {self.apellido} {self.cliente_pais}"
    
class Producto(models.Model):
    nombre = models.CharField(max_length=150)
    descripcion = models.TextField(blank=True, null=True)
    precio = models.DecimalField(max_digits=10, decimal_places=0)
    stock = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.nombre