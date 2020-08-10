from django.db import models

# Create your models here.
class Pedidos(models.Model):
    num_pedido = models.CharField(max_length=30)
    cliente = models.CharField(max_length=30)
    valor = models.CharField(max_length=30)
    productos = models.CharField(max_length=30)

class Clientes(models.Model):
    nombre = models.CharField(max_length=30)
    direccion = models.CharField(max_length=50)
    telefono = models.CharField(max_length=30)
    email = models.EmailField()
    telefono = models.CharField(max_length=30)

class Productos(models.Model):
    descripcion = models.CharField(max_length=30)
    codigo = models.CharField(max_length=50)
    valor = models.CharField(max_length=30)
    categoria = models.CharField(max_length=30)
