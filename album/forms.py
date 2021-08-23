from django import forms
from album.models import Album
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from maintenance.models import Artista, SelloDiscografico, GeneroMusical

# edit your forms here


class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = [
            "nombre",
            "año",
            "artista",
            "sello",
            "genero",
        ]
        labels = {
            "nombre": "Nombre",
            "año": "Año",
            "artista": "Artista",
            "sello": "Sello",
            "genero": "Genero",
        }

    nombre = forms.CharField()
    año = forms.CharField()
    artista = forms.ModelChoiceField(
        queryset=Artista.objects.all(), widget=forms.Select
    )
    sello = forms.ModelChoiceField(queryset=SelloDiscografico.objects.all())
    genero = forms.ModelChoiceField(queryset=GeneroMusical.objects.all())
    nombre.widget = forms.TextInput(attrs={"class": "form-control"})
    año.widget = forms.TextInput(attrs={"class": "form-control"})
    artista.widget = forms.Select(attrs={"class": "form-select"})
    sello.widget = forms.Select(attrs={"class": "form-select"})
    genero.widget = forms.Select(attrs={"class": "form-select"})
