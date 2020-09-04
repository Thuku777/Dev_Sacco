from django.shortcuts import render

from .models import *

# Create your views here.
def service(request):
    service = Service.objects.all()
    return render(request, 'service.html', {'service': service})