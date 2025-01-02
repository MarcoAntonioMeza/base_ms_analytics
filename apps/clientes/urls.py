from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required



urlpatterns = [
    path('',                 login_required(views.index), name='clientes_index'),
    path('create/',          login_required(views.create), name='clientes_create'),
    path('view/<int:id>/',   login_required(views.view), name='cliente_view'),
    path('update/<int:id>/', login_required(views.update), name='cliente_update'),
    path('delete/<int:id>/', login_required(views.delete), name='cliente_delete'),
    
    
    
    
    
    
    #AJAX
    path('cliente-list-ajax/', login_required(views.index_list_ajax), name='list_ajax_clientes'),
    
]