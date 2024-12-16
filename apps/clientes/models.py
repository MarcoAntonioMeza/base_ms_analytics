from django.db import models

# Create your models here.
class Cliente(models.Model):
    
    LEAD = 10
    CLIENTE = 20
    
    TIPO_CHOICES = [
        (LEAD,'LEAD'),
        (CLIENTE,'CLIENTE'),
    ]
    
    nombres = models.CharField(max_length=150,verbose_name="Nombres")
    apellidos = models.CharField(max_length=150,verbose_name="Apellidos")
    telefono = models.CharField(max_length=10,verbose_name="Teléfono")
    email = models.EmailField(verbose_name="Correo electrónico")
    tipo = models.IntegerField(choices=TIPO_CHOICES,default=LEAD,verbose_name="Tipo")
    
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def save(self, *args, **kwargs):
        # Eliminar espacios extra y convertir a mayúsculas
        self.nombres = self.nombres.strip().upper()
        self.apellidos = self.apellidos.strip().upper()
        
        # Llama al método save original para guardar el objeto
        super(Cliente, self).save(*args, **kwargs)
    
    
    def __str__(self):
        return self.nombres