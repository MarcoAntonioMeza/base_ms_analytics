from rest_framework import serializers
from django.utils.timesince import timesince
from ..models import Comentario

class ComentarioSerializer(serializers.ModelSerializer):
    # Agregar un campo para el username del autor
    autor = serializers.ReadOnlyField(source='autor.username')  # 'autor' es el campo relacionado con el usuario
    fecha_creacion = serializers.SerializerMethodField()
    

    class Meta:
        model = Comentario
        fields = ['id', 'contenido', 'autor', 'fecha_creacion']
        #extra_kwargs = {'fecha_creacion': {'format': f"Hace {timesince(fecha_creacion)}"}}
    
    def get_fecha_creacion(self, obj):
        # Usar timesince para obtener la diferencia de tiempo
        return f"Hace {timesince(obj.fecha_creacion)}" 