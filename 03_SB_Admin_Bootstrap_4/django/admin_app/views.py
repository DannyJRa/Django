from django.shortcuts import render

def index(request):
    return render(request, 'admin_app/dashboard.html')

def charts(request):
    return render(request, 'admin_app/charts.html')
                  
