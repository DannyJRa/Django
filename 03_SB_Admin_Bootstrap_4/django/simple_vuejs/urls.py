from django.urls import path
#needed for url()
from django.conf.urls import url

from . import views


app_name = 'simple_vuejs'
urlpatterns = [
    path('', views.index, name='index'),

]