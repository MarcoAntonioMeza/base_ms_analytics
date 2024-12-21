from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    
    path('admin/', admin.site.urls),
    
    path("usuario/", include("apps.usuario.urls")),
    path("simulador/", include("apps.simulador.urls")),
    path("direccion/", include("direccion.urls")),
    
    
    path("", include("apps.home.urls")),  
    #static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    # UI Kits Html files
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#if settings.DEBUG:
#    urlpatterns += static(settings.MEDIA_ROOT, document_root=settings.MEDIA_ROOT)