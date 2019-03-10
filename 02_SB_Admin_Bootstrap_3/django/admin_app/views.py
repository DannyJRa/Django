from django.shortcuts import render

def index(request):
    return render(request, 'admin_app/dashboard.html')

def tables(request):
    return render(request, 'admin_app/tables.html')

def flot(request):
    return render(request, 'admin_app/flot.html')

def morris(request):
    return render(request, 'admin_app/morris.html')

def forms(request):
    return render(request, 'admin_app/forms.html')

def panels_wells(request):
    return render(request, 'admin_app/panels_wells.html')

def buttons(request):
    return render(request, 'admin_app/buttons.html')

def notifications(request):
    return render(request, 'admin_app/notifications.html')

def typography(request):
    return render(request, 'admin_app/typography.html')

def icons(request):
    return render(request, 'admin_app/icons.html') 

def grid(request):
    return render(request, 'admin_app/grid.html')   

def blank(request):
    return render(request, 'admin_app/blank.html')

def login(request):
    return render(request, 'admin_app/login.html')                     
