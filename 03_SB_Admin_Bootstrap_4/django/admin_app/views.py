from django.shortcuts import render

def index(request):
    return render(request, 'admin_app/dashboard.html')

def charts(request):
    return render(request, 'admin_app/charts.html')
                  
def buttons(request):
    return render(request, 'admin_app/buttons.html')

def utilities_animation(request):
    return render(request, 'admin_app/utilities_animation.html')

def chart_csv(request):
    return render(request, 'admin_app/chart_csv.html')

def tables(request):
    return render(request, 'admin_app/tables.html')

def cards(request):
    return render(request, 'admin_app/cards.html')
######## Chart.js

from django.http import JsonResponse
from django.views.generic import View




## Option 1: Hard-coded
class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'admin_app/charts_chartjs.html', {"customers": 10})


def get_data(request, *args, **kwargs):
    data = {
        "sales": 100,
        "customers": 10,
    }
    return JsonResponse(data) # http response


## Option 3
#pip install djangorestframework
from rest_framework.views import APIView
from rest_framework.response import Response

from django.contrib.auth import get_user_model
User = get_user_model()

class ChartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        #qs_count = User.objects.all().count()
        labels = ["Users", "Blue", "Yellow", "Green", "Purple", "Orange"]
        default_items = [1, 23, 2, 3, 12, 2]
        data = {
                "labels": labels,
                "default": default_items,
                #"users": User.objects.all().count()
        }
        return Response(data)