from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('drinkmilo', views.drinkmilo),
    path('reset', views.reset),
    path('drinkmilo2', views.drinkmilo2),
    path('reset2', views.reset2),
]