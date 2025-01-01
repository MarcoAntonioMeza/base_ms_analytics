from django.urls import path
from . import views
from django.conf.urls import handler404
from apps.adminv2.views import pag_404_not_found

#handler404 = pag_404_not_found
#handler404 = "apps.adminv2.views.pag_404_not_found"


urlpatterns = [
    path('', views.index, name='clientes_index'),
    path('create/', views.create, name='clientes_create'),
    path('view/<int:id>/', views.view, name='cliente_view'),
    path('update/<int:id>/', views.update, name='cliente_update'),
    path('delete/<int:id>/', views.delete, name='cliente_delete'),
    
    
    
    
    
    
    #AJAX
    path('cliente-list-ajax/', views.index_list_ajax, name='list_ajax_clientes'),
    
]