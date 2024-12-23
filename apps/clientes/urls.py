from django.urls import path,re_path
from . import views

urlpatterns = [
    path('', views.index, name='clientes_index'),
    
    
    
    
    
    
    #AJAX
    path('cliente-list-ajax/', views.index_list_ajax, name='list_ajax_clientes'),
    
]