from django.urls import path,re_path
from apps.simulador import views 


urlpatterns = [
    path('', views.index, name='index'),
    re_path(r'^.*\.*', views.pages, name='pages'),
   
]