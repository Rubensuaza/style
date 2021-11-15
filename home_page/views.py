from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request,template_name='templates_home/index.html')

def service_1(request):
    return render(request,template_name='templates_home/servicio1.html')

def whoAre(request):
    return render(request,template_name='templates_home/presentation.html')