from django.urls import path
from CrmApp import views

urlpatterns = [
    path('', views.home, name="Home"),
    path('prospecto/', views.prospecto, name="Prospecto"),
    path('oportunidad/', views.oportunidad, name="Oportunidad"),
    path('pedido/', views.pedido, name="Pedido"),
]
