from django.db import models
from datetime import datetime
from direccion.models import   CodigoPostal, Estado, Municipio, Colonia

# Create your models here.
class Cliente(models.Model):
    
    class Meta:
        permissions = [
            ("can_view_cliente", "VER CLIENTE"),
            ("can_update_cliente", "ACTUALIZAR CLIENTE"),
            ("can_create_cliente", "CREAR CLIENTE"),
            ("can_delete_cliente", "ELIMINAR CLIENTE"),
        ]
        
    
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
    status = models.IntegerField(choices=ESTADO_CHOICES,default=ACTIVO,verbose_name="Status")
    giro = models.CharField(max_length=255,verbose_name="Giro",null=True,blank=True,default=None)
    fecha_nacimiento = models.DateField(verbose_name="Fecha de nacimiento",null=True,blank=True,default=None)
    created_at = models.DateTimeField(default=None,null=True)
    updated_at = models.DateTimeField(default=None,null=True)
    
    def save(self, *args, **kwargs):
        # Eliminar espacios extra y convertir a mayúsculas
        self.nombres = self.nombres.strip().upper()
        self.apellido_paterno = self.apellido_paterno.strip().upper()
        self.apellido_materno = self.apellido_materno.strip().upper()

        # Establecer las fechas de creación y actualización
        if not self.created_at:
            self.created_at = datetime.now()
        else:
            self.updated_at = datetime.now()
        

        # Llama al método save original para guardar el objeto
        super().save(*args, **kwargs)
    
    
    def __str__(self):
        return self.nombres
    
    def full_name(self):
        return f"{self.nombres} {self.apellido_paterno} {self.apellido_materno}"
    
    


class DireccionClientes(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='direcciones')
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)
    municipio = models.ForeignKey(Municipio, on_delete=models.CASCADE)
    codigo_postal = models.ForeignKey(CodigoPostal, on_delete=models.CASCADE,null=True)
    colonia = models.ForeignKey(Colonia, on_delete=models.CASCADE)
    calle = models.CharField(max_length=200)
    numero_exterior = models.CharField(max_length=20, null=True, blank=True)
    numero_interior = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return f"{self.calle}, {self.colonia}, {self.municipio.nombre}, {self.estado.nombre}"
    
    
    def save(self, *args, **kwargs):
        

        # Establecer las fechas de creación y actualización
        if not self.numero_exterior:
            self.numero_exterior = ""
        
        if not self.numero_interior:
            self.numero_interior = ""
        
        

        # Llama al método save original para guardar el objeto
        super().save(*args, **kwargs)