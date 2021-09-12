from django.urls import path
from app1 import views

app_name = 'app1'

urlpatterns = [
    path('relative/', views.relative, name='relative'),
    path('other/', views.other, name='other'),
    ]

    