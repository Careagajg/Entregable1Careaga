from django import forms


class ClientesFormulario(forms.Form):

    #Especificar los campos
    nombre = forms.CharField()
    apellido = forms.CharField()
    ordenCompra = forms.IntegerField()


class VentasFormulario(forms.Form):   
    mes = forms.CharField(max_length=30)
    totalV = forms.IntegerField()


class CostosFormulario(forms.Form):   
    mes = forms.CharField(max_length=30)
    totalC = forms.IntegerField()