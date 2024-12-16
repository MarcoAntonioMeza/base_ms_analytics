from django.db import models
from direccion.models import Estado
from apps.clientes.models import Cliente
# Create your models here.

class Solicitud(models.Model):
  
    consumo_kwh = models.IntegerField(verbose_name="Consumo (kWh)")
    pago = models.DecimalField(verbose_name="Pago",max_digits=10, decimal_places=2)
    estdo_name = models.CharField(max_length=50)
    estado  = models.ForeignKey(Estado, on_delete=models.CASCADE,verbose_name="Estado")
    cantidad_energia_ahorrada = models.IntegerField(verbose_name="Cantidad de energía a ahorrar %")
    
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE,verbose_name="Cliente")
    
    created_at = models.DateTimeField(verbose_name="Fecha de creación",auto_now_add=True)
