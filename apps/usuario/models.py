import os
import uuid
from django.contrib.auth.models import AbstractUser
from django.db import models
import time

class Usuario(AbstractUser):
    profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
    nombre = models.CharField(max_length=200, null=False, verbose_name='Primer Nombre')
    segundo_nombre = models.CharField(max_length=200, null=True, verbose_name='Segundo Nombre')
    apellido_paterno = models.CharField(max_length=200, null=True, verbose_name='Apellido Paterno')
    apellido_materno = models.CharField(max_length=200, null=True, verbose_name='Apellido Materno')
    access_to_app = models.BooleanField(default=True, verbose_name='Puede acceder a la app')
    
    bio = models.TextField(null=True, blank=True, verbose_name='Biografía')
    amigos = models.ManyToManyField('self', blank=True, symmetrical=True, related_name='amigos_conectados', verbose_name='Amigos')
    name_soacial_media = models.CharField(max_length=200, null=True, blank=True, verbose_name='Nombre de la red social')

    created_at = models.IntegerField(default=None, null=True, verbose_name='Fecha de creación')
    updated_at = models.IntegerField(default=None,null=True, verbose_name='Fecha de actualización')
    created_by = models.ForeignKey(
        'self', 
        null=True, 
        blank=True, 
        on_delete=models.SET_NULL, 
        related_name='usuarios_creados',
        verbose_name='Creado por'
    )
    updated_by = models.ForeignKey(
        'self', 
        null=True, 
        blank=True, 
        on_delete=models.SET_NULL, 
        related_name='usuarios_actualizados',
        verbose_name='Actualizado por'
    )

    def full_name(self):
        return f"{self.nombre} {self.segundo_nombre or ''} {self.apellido_paterno} {self.apellido_materno}"
    
    def __str__(self):
        return self.username
    
    
    
    def save(self, *args, **kwargs):
        # Cambiar el nombre del archivo de la imagen a un nombre único aleatorio
        if self.profile_picture:
            # Obtener la extensión del archivo
            ext = self.profile_picture.name.split('.')[-1]
            # Generar un nuevo nombre de archivo utilizando uuid
            new_name = f"{uuid.uuid4().hex}.{ext}"
            # Asignar el nuevo nombre al campo 'profile_picture'
            self.profile_picture.name = os.path.join(new_name)
        # Si el objeto es nuevo (es decir, no tiene created_at), asignamos la fecha de creación
        if not self.created_at:
            self.created_at = int(time.time())
        else:
            # Actualizamos la fecha de modificación cada vez que se guarda el objeto
            self.updated_at = int(time.time())
        
        # Llamamos al método save original para guardar el objeto
        super(Usuario, self).save(*args, **kwargs)
