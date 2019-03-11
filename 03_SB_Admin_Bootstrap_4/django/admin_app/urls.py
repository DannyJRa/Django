
from django.urls import path
#needed for url()
from django.conf.urls import url

from . import views
from .views import HomeView, get_data, ChartData

app_name = 'admin_app'
urlpatterns = [
    path('', views.index, name='index'),
    path('charts', views.charts, name='charts'),
    path('buttons', views.buttons, name='buttons'),
    path('utilities_animation', views.utilities_animation, name='utilities_animation'),
    path('chart_csv', views.chart_csv, name='chart_csv'),
   # path('charts_chartjs', views.HomeView, name='charts_chartjs.html'),


    path('tables', views.tables, name='tables'),
    url('api/data/', get_data, name='api-data'),
    url('api/chart/data/', ChartData.as_view()),
    url('test', HomeView.as_view(), name='home'),
]