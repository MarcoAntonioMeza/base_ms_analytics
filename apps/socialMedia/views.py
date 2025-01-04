# views.py
from django.shortcuts import render, redirect
from rest_framework.response import Response
from rest_framework.decorators import api_view
from apps.usuario.models import Usuario
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from datetime import datetime
from django.utils.timesince import timesince

import locale
locale.setlocale(locale.LC_TIME, 'es_MX.UTF-8')
from .models import Publicacion, Comentario, MeGustaPublicacion, MeGustaComentario
from .serializers.comentario import ComentarioSerializer
# Vista para la página principal donde se muestran las publicaciones

def home(request):
    publicaciones = Publicacion.objects.all().order_by('-fecha_creacion')
    return render(request, 'social_media/home/index.html', {'publicaciones': publicaciones})


#@login_required
#@csrf_exempt
#def comentar_publicacion(request):
#    if request.method == 'POST':
#        contenido = request.POST.get('contenido')
#        publicacion_id = request.POST.get('publicacion_id')
#        
#        if not contenido or not publicacion_id:
#            return JsonResponse({"message": "Faltan datos","staus_code":10}, status=400)
#        
#        publicacion = Publicacion.objects.get(id=publicacion_id)
#        comentario = Comentario(publicacion=publicacion, autor=request.user, contenido=contenido)
#        comentario.save()
#
#        # Convertir el comentario en un diccionario para serialización JSON
#        comentario_data = {
#            'id': comentario.id,
#            'contenido': comentario.contenido,
#            'autor': comentario.autor.username,  # O cualquier otro campo que necesites
#            'fecha_creacion': comentario.fecha_creacion.strftime('%Y-%m-%d %H:%M:%S')  # Formato de fecha
#        }
#
#        return JsonResponse({
#            "message": "Comentario agregado",
#            "comentario": comentario_data,
#            "staus_code": 10
#        }, status=200)
@api_view(['POST'])
def comentar_publicacion(request):
    if request.method == 'POST':
        contenido = request.POST.get('contenido')
        publicacion_id = request.POST.get('publicacion_id')
        
        if not contenido or not publicacion_id:
            return Response({"message": "Faltan datos", "status_code": 10}, status=400)
        
        publicacion = Publicacion.objects.get(id=publicacion_id)
        comentario = Comentario(publicacion=publicacion, autor=request.user, contenido=contenido)
        comentario.save()

        # Serializamos el comentario
        serializer = ComentarioSerializer(comentario)

        return Response({
            "message": "Comentario agregado",
            "comentario": serializer.data,  # Serializado a JSON
            "status_code": 10
        }, status=200)
# Vista para dar "me gusta" a una publicación
@login_required
def me_gusta_publicacion(request, publicacion_id):
    publicacion = Publicacion.objects.get(id=publicacion_id)
    me_gusta = MeGustaPublicacion(publicacion=publicacion, usuario=request.user)
    me_gusta.save()
    return JsonResponse({"message": "Me gusta agregado"}, status=200)

# Vista para dar "me gusta" a un comentario
@login_required
def me_gusta_comentario(request, comentario_id):
    comentario = Comentario.objects.get(id=comentario_id)
    me_gusta = MeGustaComentario(comentario=comentario, usuario=request.user)
    me_gusta.save()
    return JsonResponse({"message": "Me gusta agregado al comentario"}, status=200)



@csrf_exempt
def crear_publicacion(request):
    if request.method == 'POST':
        contenido = request.POST.get('contenido')
        imagen = request.FILES.get('imagen')
        autor = request.user  # Usuario autenticado
        publicacion = Publicacion.objects.create(contenido=contenido, imagen=imagen, autor=autor)
        return JsonResponse({
            'id': publicacion.id,
            'autor': publicacion.autor.username,
            'contenido': publicacion.contenido,
            'imagen': publicacion.imagen.url if publicacion.imagen else None,
            'fecha_creacion': timesince(publicacion.fecha_creacion) , #publicacion.fecha_creacion.strftime('%Y-%m-%d %H:%M:%S'),
            'reacciones': publicacion.count_likes,#publicacion.reacciones,
            'comentarios': []
        })

def obtener_publicaciones(request):
   
    
    data =  Publicacion.get_publicaciones()
    return JsonResponse(data, safe=False)

@csrf_exempt
def reaccionar_publicacion(request):
    if request.method == 'POST':
        publicacion_id = request.POST.get('publicacion_id')
        
        publicacion = get_object_or_404(Publicacion, id=publicacion_id)
        publicacion.aumentar_likes()
        
        return JsonResponse({'reacciones': publicacion.count_likes})


