from django.urls import path

from AppEntregable1 import views

urlpatterns = [
   
    path('', views.inicio, name="Inicio"), 
    path('clientes', views.clientes, name="Clientes"),
    path('ventas', views.ventas, name="Ventas"),
    path('costos', views.costos, name="Costos"),
    path('ClientesFormulario', views.ClientesFormulario, name="ClientesFormulario"),
    path('VentasFormulario', views.VentasFormulario, name="VentasFormulario"),
    path('CostosFormulario', views.CostosFormulario, name="CostosFormulario"),
    path('buscar', views.buscar),

]


   