from django import forms
from maintenance.models import Artista, SelloDiscografico, GeneroMusical
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# edit your forms here


class ArtistaForm(forms.ModelForm):
    class Meta:
        model = Artista
        fields = [
            "nombre",
        ]
        labels = {
            "nombre": "Nombre",
        }
        widgets = {
            "nombre": forms.TextInput(attrs={"class": "form-control"}),
        }


class SelloForm(forms.ModelForm):
    class Meta:
        model = SelloDiscografico
        fields = [
            "nombre",
        ]
        labels = {
            "nombre": "Nombre",
        }
        widgets = {
            "nombre": forms.TextInput(attrs={"class": "form-control"}),
        }


class GeneroForm(forms.ModelForm):
    class Meta:
        model = GeneroMusical
        fields = [
            "nombre",
        ]
        labels = {
            "nombre": "Nombre",
        }
        widgets = {
            "nombre": forms.TextInput(attrs={"class": "form-control"}),
        }
