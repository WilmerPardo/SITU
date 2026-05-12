from django import forms
from .models import Pasajero

class PasajeroFormulario(forms.ModelForm):
	class Meta:
		model = Pasajero
		fields=["cedula","nombre","apellido", "email","imagen"] 
		#fields = '__all__'