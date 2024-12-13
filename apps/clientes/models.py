from django.db import models

# Create your models here.
class Cliente(models.Model):
    
    LEAD = 10
    CLIENTE = 20
    
    TIPO_CHOICES = [
        (LEAD,'LEADS'),
        (CLIENTE,'CLIENTES'),
    ]
    
    nombres = models.CharField(max_length=150,verbose_name="Nombres")
    apellidos = models.CharField(max_length=150,verbose_name="Apellidos")
    telefono = models.CharField(max_length=10,verbose_name="Teléfono")
    email = models.EmailField(verbose_name="Correo electrónico")
    tipo = models.IntegerField(choices=TIPO_CHOICES,default=LEAD,verbose_name="Tipo")
    
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return self.nombres