from django.db import models

# Create your models here.

class Clientes(models.Model):

    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    ordenCompra = models.IntegerField()
    


class Ventas(models.Model):
    mes = models.CharField(max_length=30)
    totalV = models.IntegerField()
    

class Costos(models.Model):
    mes = models.CharField(max_length=30)
    totalC = models.IntegerField()

