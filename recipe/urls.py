# urls.py
from django.urls import path
from . import views
from .views import get_recipe 

urlpatterns = [
    path('', views.home, name='home'), # Maps to the home function in views.py
    path('home/register', views.register, name='register'),
    path('home/homie', views.homie, name='homie'), # Note the trailing slash
    path('home/homie/ap1', views.ap1, name='ap1'), 
    path('home/homie/ap2', views.ap2, name='ap2'), 
    path('home/homie/ap3', views.ap3, name='ap3'), 
    path('home/homie/ap4', views.ap4, name='ap4'), 
    path('home/homie/ap7', views.ap7, name='ap7'), 
    path('home/homie/ai', views.ai, name='ai'),
    path('home/homie/yours', views.yours, name='yours'),
    path('home/homie/ai/get-recipe', views.get_recipe, name='get_recipe'),
]
