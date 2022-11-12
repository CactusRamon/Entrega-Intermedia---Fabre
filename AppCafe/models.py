from django.db import models

# Create your models here.

class Cafe(models.Model):

    nombre = models.CharField(max_length=50)
    origen = models.CharField(max_length=50)
    tueste = models.CharField(max_length=50)

class Cafetera(models.Model):

    metodo = models.CharField(max_length=50)
    nombre = models.CharField(max_length=50)
  
class Herramienta(models.Model):

    nombre = models.CharField(max_length=50)
