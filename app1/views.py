from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse("<h1>App 1</h1")


def main(request):
    return render(request, 'index.html')