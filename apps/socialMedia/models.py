import os
import uuid
from django.db import models
from apps.usuario.models import Usuario

class Publicacion(models.Model):
    autor = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='publicaciones', verbose_name='Autor')
    contenido = models.TextField(verbose_name='Contenido de la Publicación')
    imagen = models.ImageField(upload_to='post_images/', null=True, blank=True, verbose_name='Imagen')
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')

    def __str__(self):
        return f"Publicación de {self.autor.username} el {self.fecha_creacion.strftime('%Y-%m-%d %H:%M:%S')}"
    
    def save(self, *args, **kwargs):
        # Cambiar el nombre del archivo de la imagen a un nombre único aleatorio
        if self.imagen:
            ext = self.imagen.name.split('.')[-1]
            new_name = f"{uuid.uuid4().hex}.{ext}"
            self.imagen.name = os.path.join(new_name)
        else:
            self.imagen = None
        super(Publicacion, self).save(*args, **kwargs)


class Comentario(models.Model):
    publicacion = models.ForeignKey(Publicacion, on_delete=models.CASCADE, related_name='comentarios', verbose_name='Publicación')
    autor = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='comentarios', verbose_name='Autor')
    contenido = models.TextField(verbose_name='Contenido del Comentario')
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')

    def __str__(self):
        return f"Comentario de {self.autor.username} en {self.publicacion.id}"
    
    


class MeGustaPublicacion(models.Model):
    publicacion = models.ForeignKey(Publicacion, on_delete=models.CASCADE, related_name='me_gustas', verbose_name='Publicación')
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='me_gustas_publicacion', verbose_name='Usuario')

    class Meta:
        unique_together = ('publicacion', 'usuario')  # Un usuario solo puede dar un "me gusta" por publicación

    def __str__(self):
        return f"{self.usuario.username} le gustó la publicación {self.publicacion.id}"


class MeGustaComentario(models.Model):
    comentario = models.ForeignKey(Comentario, on_delete=models.CASCADE, related_name='me_gustas', verbose_name='Comentario')
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='me_gustas_comentario', verbose_name='Usuario')

    class Meta:
        unique_together = ('comentario', 'usuario')  # Un usuario solo puede dar un "me gusta" por comentario

    def __str__(self):
        return f"{self.usuario.username} le gustó el comentario {self.comentario.id}"

