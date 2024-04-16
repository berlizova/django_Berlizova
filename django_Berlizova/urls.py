"""
URL configuration for django_Berlizova project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app1 import views as views_1
from app2 import views as views_2

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app1/', views_1.app1, name='app1'),
    path('app2/', views_2.app2, name='app2'),
    path('',views_1.index, name='index'),

]
