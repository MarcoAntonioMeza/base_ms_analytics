from django.urls import path,re_path
from apps.usuario import views 
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name='user_index'),
    path('create/', views.crear_usuario, name='user_create'),
    path('update/<int:id>', views.update_usuario, name='user_update'),
    path('view/<int:id>', views.view_usuario, name='user_view'),
    path('solicitud-list-ajax/', views.index_list_ajax, name='list_ajax_usuarios'),
    path('delete/<int:id>', views.delete_usuario, name='user_delete'),
    #path('solicitud-list/', views.index_list, name='list_solicituds'),
    #path('solicitud-list-ajax/', views.index_list_ajax, name='list_solicituds_ajax'),
    
    
    
    
    #re_path(r'^.*\.*', views.pages, name='pages'),

]