from django.db import models
from direccion.models import   CodigoPostal, Estado, Municipio, Colonia

# Create your models here.
class Cliente(models.Model):
    
    LEAD = 10
    CLIENTE = 20
    
    TIPO_CHOICES = [
        (LEAD,'LEAD'),
        (CLIENTE,'CLIENTE'),
    ]
    
    ACTIVO = 10
    INACTIVO = 20
    
    ESTADO_CHOICES = [
        (ACTIVO, 'ACTIVO'),
        (INACTIVO, 'INACTIVO'),
    ]    
    nombres = models.CharField(max_length=150,verbose_name="Nombres")
    apellido_materno= models.CharField(max_length=150,verbose_name="Apellidos materno ", default=None)
    apellido_paterno= models.CharField(max_length=150,verbose_name="Apellido paterno ", default=None)
    telefono = models.CharField(max_length=10,verbose_name="Teléfono celular")
    telefono2 = models.CharField(max_length=10,verbose_name="Teléfono celular 2",null=True,blank=True,default=None)
    email = models.EmailField(verbose_name="Correo electrónico")
    tipo = models.IntegerField(choices=TIPO_CHOICES,default=LEAD,verbose_name="Tipo")
    estado = models.IntegerField(choices=ESTADO_CHOICES,default=ACTIVO,verbose_name="Estado")
    giro = models.CharField(max_length=255,verbose_name="Giro",null=True,blank=True,default=None)
    fecha_nacimiento = models.DateField(verbose_name="Fecha de nacimiento",null=True,blank=True,default=None)
    
    
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
    
    


class DireccionClientes(models.Model):
    usuario = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='direcciones')
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)
    municipio = models.ForeignKey(Municipio, on_delete=models.CASCADE)
    codigo_postal = models.ForeignKey(CodigoPostal, on_delete=models.CASCADE)
    colonia = models.ForeignKey(Colonia, on_delete=models.CASCADE)
    calle = models.CharField(max_length=200)
    numero_exterior = models.CharField(max_length=20, null=True, blank=True)
    numero_interior = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return f"{self.calle}, {self.colonia}, {self.municipio.nombre}, {self.estado.nombre}"