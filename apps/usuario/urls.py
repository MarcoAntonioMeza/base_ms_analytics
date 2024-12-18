from django.urls import path,re_path
from apps.usuario import views 


urlpatterns = [
    path('', views.index, name='user_index'),
    
    path('create/', views.crear_usuario, name='user_create'),
    #path('solicitud-list/', views.index_list, name='list_solicituds'),
    #path('solicitud-list-ajax/', views.index_list_ajax, name='list_solicituds_ajax'),
    
    
    
    
    #re_path(r'^.*\.*', views.pages, name='pages'),

]