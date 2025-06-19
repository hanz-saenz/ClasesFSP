from django.contrib import admin
from .models import Categoria, Proveedor, Marca, Producto, Imagen
# Register your models here.

admin.site.register(Categoria)
admin.site.register(Proveedor)
admin.site.register(Marca)
admin.site.register(Producto)
admin.site.register(Imagen)