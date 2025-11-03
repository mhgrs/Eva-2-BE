# djangoTecnoFelipe/forms.py
from django import forms
from .models import Producto, Cliente

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__' 

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'
        widgets = {
            'fechaNacimiento': forms.DateInput(attrs={'type': 'date'}),
            'fechaRegistro': forms.DateInput(attrs={'type': 'date', 'readonly': True}),
        }