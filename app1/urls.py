from django.urls import path
from .views import index, main

app_name = 'app1'

urlpatterns = [
       path('', index, name='index'),


]