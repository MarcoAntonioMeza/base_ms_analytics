import os
import uuid
from django.db import models
from django.templatetags.static import static
from django.utils.timesince import timesince
from apps.usuario.models import Usuario

class Publicacion(models.Model):
    autor = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='publicaciones', verbose_name='Autor')
    contenido = models.TextField(verbose_name='Contenido de la Publicación')
    imagen = models.ImageField(upload_to='post_images/', null=True, blank=True, verbose_name='Imagen')
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')
    count_likes = models.IntegerField(default=0, verbose_name='Número de Me Gusta')
    
    #reaciones = models.ManyToManyField(Usuario, through='MeGustaPublicacion', related_name='reacciones', verbose_name='Reacciones')


    def aumentar_likes(self):
        self.count_likes += 1
        self.save()
    
    def disminuir_likes(self):
        if self.count_likes > 0:
            self.count_likes -= 1
            self.save()
    
    def __str__(self):
        return f"Publicación de {self.autor.username} el {self.fecha_creacion.strftime('%Y-%m-%d %H:%M:%S')}"
    
    @staticmethod
    def get_publicaciones(user_id=None):
        publicaciones = Publicacion.objects.all().order_by('-fecha_creacion')
        data = []
        for pub in publicaciones:
            data.append({
                'id': pub.id,
                'autor': pub.autor.username,
                'autor_image': pub.autor.profile_picture.url if pub.autor.profile_picture else static('/assets/img/brand/icon_user.png'),
                'contenido': pub.contenido,
                'imagen': pub.imagen.url if pub.imagen else None,

                'fecha_creacion': f"Hace {timesince(pub.fecha_creacion)} ", #.strftime('%d de %B de %Y %H:%M:%S'),
                'reacciones': pub.count_likes,#pub.reacciones,
                'mostrarComentarios': False,
                'comentarios': [
                    {'id': com.id, 'autor': com.autor.username, 'contenido': com.contenido, 'fecha_creacion': f"Hace {timesince(com.fecha_creacion)} "} #com.fecha_creacion.strftime('%d de %B de %Y %H:%M:%S')}
                    for com in pub.comentarios.all()
                ]
            })
        return data
    
    def save(self, *args, **kwargs):
        # Solo cambiar el nombre del archivo si es una nueva imagen
        if self.imagen and not self.pk:  # Solo si es una nueva instancia
            ext = self.imagen.name.split('.')[-1]
            new_name = f"{uuid.uuid4().hex}.{ext}"
            self.imagen.name = os.path.join(new_name)
        elif not self.imagen and self.pk:
            # Mantener la imagen actual si no se proporciona una nueva en la actualización
            old_instance = Publicacion.objects.get(pk=self.pk)
            self.imagen = old_instance.imagen
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

