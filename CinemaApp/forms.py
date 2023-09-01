from django import forms

# Formulario de Usuarios
class UserForm(forms.Form):
    name = forms.CharField(required=True)
    surname = forms.CharField(required=True)
    dni = forms.CharField(required=True)
    email = forms.EmailField(required=True)

#Widget para darle formato date al release en MovieForm
class DateInput(forms.DateInput):
    input_type = 'date'

# Formulario de peliculas
class MovieForm(forms.Form):
    movie = forms.CharField(required=True)
    genre = forms.CharField(required=True)
    release = forms.DateField(widget=DateInput)
    
# Formulario de Cines   
class CinemaForm(forms.Form):
    name = forms.CharField(required=True)
    location = forms.CharField(required=True)
    capacity = forms.IntegerField(required=True )
    
