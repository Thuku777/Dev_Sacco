from django.shortcuts import render
from django.http import HttpResponse

from .models import About


def index(request):
    return render(request, 'pages/index.html')


def about(request):
    about = About.objects.all()
    return render(request, 'pages/about.html', {'about': about})

