from django.contrib.auth.models import AbstractUser
from django.db import models


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

    created_at = models.IntegerField(default=None, verbose_name='Fecha de creación')
    updated_at = models.IntegerField(default=None, verbose_name='Fecha de actualización')
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
