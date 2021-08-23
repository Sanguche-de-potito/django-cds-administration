from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from maintenance.models import Artista, SelloDiscografico, GeneroMusical
from maintenance.forms import ArtistaForm, SelloForm, GeneroForm
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.core import serializers
import json


# Create your views here.


def index(request):
    return render(request, "maintenance/maintenance_list.html")


def artista_serializers(request):
    lista = serializers.serialize("json", Artista.objects.all())
    return HttpResponse(lista, content_type="application/json")


def sello_serializers(request):
    lista = serializers.serialize("json", SelloDiscografico.objects.all())
    return HttpResponse(lista, content_type="application/json")


def genero_serializers(request):
    lista = serializers.serialize("json", GeneroMusical.objects.all())
    return HttpResponse(lista, content_type="application/json")


class ArtistaCreate(CreateView):
    model = Artista
    form_class = ArtistaForm
    template_name = "maintenance/artista_form.html"
    success_url = reverse_lazy("maintenance:maintenance_index")


class SelloCreate(CreateView):
    model = SelloDiscografico
    form_class = SelloForm
    template_name = "maintenance/sello_form.html"
    success_url = reverse_lazy("maintenance:maintenance_index")


class GeneroCreate(CreateView):
    model = GeneroMusical
    form_class = GeneroForm
    template_name = "maintenance/genero_form.html"
    success_url = reverse_lazy("maintenance:maintenance_index")


class ArtistaUpdate(UpdateView):
    model = Artista
    form_class = ArtistaForm
    template_name = "maintenance/artista_form.html"
    success_url = reverse_lazy("maintenance:maintenance_index")


class SelloUpdate(UpdateView):
    model = SelloDiscografico
    form_class = SelloForm
    template_name = "maintenance/sello_form.html"
    success_url = reverse_lazy("maintenance:maintenance_index")


class GeneroUpdate(UpdateView):
    model = GeneroMusical
    form_class = GeneroForm
    template_name = "maintenance/genero_form.html"
    success_url = reverse_lazy("maintenance:maintenance_index")


class ArtistaDelete(DeleteView):
    model = Artista
    template_name = "maintenance/artista_delete.html"
    success_url = reverse_lazy("maintenance:maintenance_index")


class SelloDelete(DeleteView):
    model = SelloDiscografico
    template_name = "maintenance/sello_delete.html"
    success_url = reverse_lazy("maintenance:maintenance_index")


class GeneroDelete(DeleteView):
    model = GeneroMusical
    template_name = "maintenance/genero_delete.html"
    success_url = reverse_lazy("maintenance:maintenance_index")
