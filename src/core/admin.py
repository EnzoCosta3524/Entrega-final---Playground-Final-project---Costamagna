from django.contrib import admin
from .models import Cliente, Pais, Producto

admin.site.register(Cliente)
admin.site.register(Pais)
admin.site.register(Producto)