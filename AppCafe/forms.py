from django import forms

class CafeFormulario(forms.Form):
    nombre = forms.CharField()
    origen = forms.CharField()
    tueste = forms.CharField()

class CafeteraFormulario(forms.Form):
    metodo = forms.CharField()
    nombre = forms.CharField()

class HerramientaFormulario(forms.Form):
    nombre = forms.CharField()