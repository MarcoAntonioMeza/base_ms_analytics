from django.urls import path,re_path
from apps.simulador import views 


urlpatterns = [
    path('', views.index, name='simulador_index'),
    path('view/<int:id>', views.detail_simulacion, name='detalle_simulacion'),
    path('solicitud-list/', views.index_list, name='list_solicituds'),
    path('solicitud-list-ajax/', views.index_list_ajax, name='list_solicituds_ajax'),
    
    
    
    
    re_path(r'^.*\.*', views.pages, name='pages'),

]