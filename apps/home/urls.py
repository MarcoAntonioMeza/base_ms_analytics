from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required

from django.urls import path, re_path
from apps.home import views

urlpatterns = [

    # The home page
    path('', login_required(views.index), name='home'),

    # Matches any html file
    #re_path(r'^.*\.*', views.pages, name='pages'),

]
