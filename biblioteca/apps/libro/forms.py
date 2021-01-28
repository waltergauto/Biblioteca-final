from django import forms
from .models import Autor, Libro

class AutorForm(forms.ModelForm):

    class Meta:
        model = Autor
        fields = [
            'nombre',
            'apellido',
            'nacionalidad',
            'descripcion'
        ]
        labels = {
            'nombre': 'Nombre del autor',
            'apellido': 'Apellido del autor',
            'nacionalidad': 'Nacionalidad del autor',
            'descripcion': 'Descripcion',
        }
        widgets = {
            'nombre': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Ingrese el nombre del autor',
                    'id': 'nombre',
                }
            ),
            'apellido': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese el apellido del autor',
                    'id': 'apellido',
                }
            ),
            'nacionalidad': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese el pais del autor',
                    'id': 'nacionalidad',
                }
            ),
            'descripcion': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese una breve descripcion',
                    'id': 'descripcion',
                }
            )
        }

class LibroForm(forms.ModelForm):

    class Meta:
        model = Libro
        fields = [
            'titulo',
            'fecha_publicacion',
            'autor'
        ]
        labels = {
            'titulo': 'Titulo del Libro',
            'fecha_publicacion': 'Fecha de Publicacion',
            'autor': 'Autor(es) del Libro',
        }
        widgets = {
            'titulo': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Ingrese el titulo del libro',
                    'id': 'titulo',
                }
            ),
            'fecha_publicacion': forms.SelectDateWidget(),
            'autor': forms.SelectMultiple(
                attrs = {
                    'class': 'form-control',
                }
            )
        }
