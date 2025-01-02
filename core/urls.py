from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import handler404, handler500, handler403, handler400
from apps.adminv2.views import pag_404_not_found
from apps.usuario import views

handler404 = "apps.adminv2.views.pag_404_not_found"
handler500 = "apps.adminv2.views.pag_500_server_error"
handler403 = "apps.adminv2.views.pag_403_forbidden"


urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    
    path("usuario/", include("apps.usuario.urls")),
    path("simulador/", include("apps.simulador.urls")),
    path("direccion/", include("direccion.urls")),
    path("clientes/", include("apps.clientes.urls")),
    path("adminv2/", include("apps.adminv2.urls")),
    
    
    path("", include("apps.home.urls")),  
    
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if not  settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    



