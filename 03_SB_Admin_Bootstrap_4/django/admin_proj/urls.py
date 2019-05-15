from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin_app/', include('admin_app.urls')),
    path('simple_vuejs/', include('simple_vuejs.urls'))
]
