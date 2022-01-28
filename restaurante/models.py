from django.db import models

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=60)

    def __str__(self):
        return self.nombre

class Platillos(models.Model):
    nombre = models.CharField(max_length=60)
    precio = models.DecimalField(max_digits=1000,decimal_places=2)
    disponible = models.IntegerField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre +' '+str(self.precio)+' '+str(self.disponible)+' '+self.categoria.nombre

class Reservaciones(models.Model):
    nombre = models.CharField(max_length=60)
    apellido = models.CharField(max_length=60)
    fecha = models.DateTimeField()
    cantidad_mesa = models.IntegerField()

    def __str__(self):
        return self.nombre +' '+self.apellido+' '+str(self.fecha)+' '+str(self.cantidad_mesa)

