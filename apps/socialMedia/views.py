# views.py
from django.shortcuts import render, redirect
from .models import Publicacion, Comentario, MeGustaPublicacion, MeGustaComentario
from apps.usuario.models import Usuario
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from datetime import datetime
import locale
locale.setlocale(locale.LC_TIME, 'es_MX.UTF-8')
# Vista para la página principal donde se muestran las publicaciones
@login_required
def home(request):
    publicaciones = Publicacion.objects.all().order_by('-fecha_creacion')
    return render(request, 'social_media/home/index.html', {'publicaciones': publicaciones})

# Vista para crear una publicación
#@login_required
#def crear_publicacion(request):
#    if request.method == 'POST':
#        contenido = request.POST.get('contenido')
#        imagen = request.FILES.get('imagen')
#        usuario = request.user
#        publicacion = Publicacion(autor=usuario, contenido=contenido, imagen=imagen)
#        publicacion.save()
#        return redirect('home')
#    return render(request, 'crear_publicacion.html')

# Vista para comentar en una publicación
@login_required
def comentar_publicacion(request, publicacion_id):
    if request.method == 'POST':
        contenido = request.POST.get('contenido')
        publicacion = Publicacion.objects.get(id=publicacion_id)
        comentario = Comentario(publicacion=publicacion, autor=request.user, contenido=contenido)
        comentario.save()
        return redirect('home')

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
            'fecha_creacion': publicacion.fecha_creacion.strftime('%d de %B de %Y %H:%M:%S') , #publicacion.fecha_creacion.strftime('%Y-%m-%d %H:%M:%S'),
            'reacciones': publicacion.count_likes,#publicacion.reacciones,
            'comentarios': []
        })

def obtener_publicaciones(request):
    data = Publicacion.get_publicaciones()
    return JsonResponse(data, safe=False)

@csrf_exempt
def reaccionar_publicacion(request):
    if request.method == 'POST':
        publicacion_id = request.POST.get('publicacion_id')
        
        publicacion = get_object_or_404(Publicacion, id=publicacion_id)
        publicacion.aumentar_likes()
        
        return JsonResponse({'reacciones': publicacion.count_likes})

@csrf_exempt
def comentar_publicacion(request, publicacion_id):
    publicacion = get_object_or_404(Publicacion, id=publicacion_id)
    contenido = request.POST.get('contenido')
    comentario = Comentario.objects.create(publicacion=publicacion, autor=request.user, contenido=contenido)
    return JsonResponse({
        'id': comentario.id,
        'autor': comentario.autor.username,
        'contenido': comentario.contenido
    })