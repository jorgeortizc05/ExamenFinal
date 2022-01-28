from django.contrib import admin
from .models import Categoria, Platillos, Reservaciones
# Register your models here.
admin.site.register(Categoria)
admin.site.register(Platillos)
admin.site.register(Reservaciones)