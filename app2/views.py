from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def app2(request):
    return HttpResponse("<h1>App 2</h1")