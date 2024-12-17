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
    
    
    def __str__(self):
        return  f"SOLICITUD DE {self.cliente.nombres} "



#==============================================================
#                           VIEWS
#==============================================================

class SimuladorSolicitudView(models.Model):
    id = models.AutoField(primary_key=True)
    consumo_kwh = models.DecimalField(max_digits=10, decimal_places=2)
    pago = models.DecimalField(max_digits=10, decimal_places=2)
    cantidad_energia_ahorrada = models.DecimalField(max_digits=10, decimal_places=2)
    cliente_id = models.IntegerField()
    estado_id = models.IntegerField()
    estado = models.CharField(max_length=255)  # Campo 'st.nombre'
    nombres = models.CharField(max_length=255)  # Campo 'cc.nombres'
    fecha = models.DateTimeField()  # Campo 's.created_at'

    class Meta:
        managed = False  # Evita que Django intente crear/modificar la vista
        db_table = 'simulador_solicitud_view'  # Nombre exacto de la vista en tu DB
        verbose_name = 'Simulador Solicitud'
        verbose_name_plural = 'Simulador Solicitudes'

    def __str__(self):
        return f"Solicitud {self.id} - {self.nombres} ({self.estado})"