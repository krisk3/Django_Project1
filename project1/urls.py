"""project1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from app1 import views
from django.conf.urls import include, url


urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('formhome/', views.form_home, name='form_home'),
    path('formpage/', views.form_name_view, name='form_name'),
    path('signuphome/', views.signup_home, name='users'),
    path('signup/', views.users, name='users'),
    path('app1/', include('app1.urls')),
    path('index2/', views.index2, name='index2'),
]


