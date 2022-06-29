from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from AppEntregable1.forms import ClientesFormulario, CostosFormulario, VentasFormulario
from AppEntregable1.models import Clientes, Ventas, Costos 

# Create your views here.

def inicio(request):

      return render(request, "AppEntregable1/inicio.html")

def clientes(request):

      return render(request, "AppEntregable1/clientes.html")

def ventas(request):

      return render(request, "AppEntregable1/ventas.html")


def costos(request):

      return render(request, "AppEntregable1/costos.html")




#Se definen los formularios 


def clientes(request):

      if request.method == 'POST':

            miFormulario = ClientesFormulario(request.POST) #aquí mellega toda la información del html

            print(miFormulario)

            if miFormulario.is_valid:   #Si pasó la validación de Django

                  informacion = miFormulario.cleaned_data

                  clientes = Clientes (nombre=informacion['nombre'], apellido=informacion['apellido'],
                  ordenCompra=informacion['ordenCompra'])

                  clientes.save()

                  return render(request, "AppEntregable1/inicio.html") #Vuelvo al inicio o a donde quieran

      else: 

            miFormulario= ClientesFormulario() #Formulario vacio para construir el html

      return render(request, "AppEntregable1/clientes.html", {"miFormulario":miFormulario})



def ventas(request):

      if request.method == 'POST':

            miFormulario = VentasFormulario(request.POST) #aquí mellega toda la información del html

            print(miFormulario)

            if miFormulario.is_valid:   #Si pasó la validación de Django

                  informacion = miFormulario.cleaned_data
                  print(informacion)
                  ventas = Ventas (mes=informacion['mes'], totalV=informacion['totalV']) 

                  ventas.save()

                  return render(request, "AppEntregable1/inicio.html") #Vuelvo al inicio o a donde quieran

      else: 

            miFormulario= VentasFormulario() #Formulario vacio para construir el html

      return render(request, "AppEntregable1/ventas.html", {"miFormulario":miFormulario})


def costos(request):

      if request.method == 'POST':

            miFormulario = CostosFormulario(request.POST) #aquí mellega toda la información del html

            print(miFormulario)

            if miFormulario.is_valid:   #Si pasó la validación de Django

                  informacion = miFormulario.cleaned_data
                  print(informacion)
                  costos = Costos (mes=informacion['mes'], totalC=informacion['totalC']) 

                  costos.save()

                  return render(request, "AppEntregable1/inicio.html") #Vuelvo al inicio 

      else: 

            miFormulario= CostosFormulario() #Formulario vacio para construir el html

      return render(request, "AppEntregable1/costos.html", {"miFormulario":miFormulario})


def buscar(request):

      if  request.GET["apellido"]: #if request.method == 'Get':

	      #respuesta = f"Estoy buscando el apellido: {request.GET['apellido'] }" 
            apellido = request.GET['apellido'] 
            print(apellido)

            clientes = Clientes.objects.filter(apellido__icontains = apellido)
            print(clientes)

            return render(request, "AppEntregable1/inicio.html", {"clientes":clientes, "apeliido":apellido})

      else: 

	      respuesta = "No enviaste datos"

            
      return render(request,"AppEntregable1/inicio.html", {"respuesta":respuesta})


