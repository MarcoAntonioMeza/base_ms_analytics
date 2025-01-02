# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home_social_media'),
    
    #path('comentar/<int:publicacion_id>/', views.comentar_publicacion, name='comentar_publicacion'),
    #path('me-gusta-publicacion/<int:publicacion_id>/', views.me_gusta_publicacion, name='me_gusta_publicacion'),
    #path('me-gusta-comentario/<int:comentario_id>/', views.me_gusta_comentario, name='me_gusta_comentario'),
    
    path('crear-publicacion/', views.crear_publicacion, name='crear_publicacion'),
    path('obtener-publicaciones/', views.obtener_publicaciones, name='obtener_publicaciones'),
    path('reaccionar-publicacion/<int:publicacion_id>/', views.reaccionar_publicacion, name='reaccionar_publicacion'),
    path('comentar-publicacion/<int:publicacion_id>/', views.comentar_publicacion, name='comentar_publicacion'),
]
