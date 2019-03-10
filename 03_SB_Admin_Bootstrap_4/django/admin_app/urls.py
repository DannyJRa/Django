from django.urls import path

from . import views

app_name = 'admin_app'
urlpatterns = [
    path('', views.index, name='index'),
    path('charts', views.charts, name='charts'),
]