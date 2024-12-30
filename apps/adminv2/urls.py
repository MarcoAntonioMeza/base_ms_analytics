from django.urls import path,re_path
from . import views

urlpatterns = [
    path('groups/', views.index, name='grupos_index'),
    path('groups/create/', views.create, name='grupos_create'),
    path('groups/view/<int:id>/', views.view, name='grupos_view'),
    path('groups/update/<int:id>/', views.update, name='grupos_update'),
    path('delete/<int:id>/', views.delete, name='grupos_delete'),
    
    
    
    
    
    
    #AJAX
    path('grupos-list-ajax/', views.index_list_ajax, name='list_ajax_grupos'),
    
]