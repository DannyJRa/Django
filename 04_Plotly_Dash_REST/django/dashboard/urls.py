from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from finance.views import company_article_list, ChartData, dash, dash_ajax

from news.views import scrape
from .views import home


urlpatterns = [
    path('admin/', admin.site.urls),
    path('notes/', include('notepad.urls', namespace='notes')),
    path('scrape/', scrape, name='scrape'),
    path('home/', home, name='home'),
    path('companies/', company_article_list, name='companies'),
    path('api/chart/data/', ChartData.as_view(), name='api-chart-data'),
    path('dash/', dash),
    path('_dash', dash_ajax),
    path('accounts/', include('allauth.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#############
#Add_Swagger 
#############
from django.conf.urls import url
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Pastebin API')

urlpatterns += [
    url(r'test$', schema_view)
]
###############