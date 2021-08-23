from django.contrib import admin
from django.urls import path
from django.contrib.auth.decorators import login_required
from maintenance.views import (
    ArtistaCreate,
    GeneroCreate,
    SelloCreate,
    ArtistaUpdate,
    GeneroUpdate,
    SelloUpdate,
    ArtistaDelete,
    GeneroDelete,
    SelloDelete,
    index,
    artista_serializers,
    sello_serializers,
    genero_serializers,
)

app_name = "maintenance"

urlpatterns = [
    path("list/", login_required(index), name="maintenance_index"),
    path("serialize/artista", artista_serializers, name="artista_listado"),
    path("serialize/genero", genero_serializers, name="genero_listado"),
    path("serialize/sello", sello_serializers, name="sello_listado"),
    path(
        "artista/create/",
        login_required(ArtistaCreate.as_view()),
        name="artista_create",
    ),
    path(
        "genero/create/", login_required(GeneroCreate.as_view()), name="genero_create"
    ),
    path("sello/create/", login_required(SelloCreate.as_view()), name="sello_create"),
    path(
        "artista/editar/<int:pk>/",
        login_required(ArtistaUpdate.as_view()),
        name="artista_update",
    ),
    path(
        "genero/editar/<int:pk>/",
        login_required(GeneroUpdate.as_view()),
        name="genero_update",
    ),
    path(
        "sello/editar/<int:pk>/",
        login_required(SelloUpdate.as_view()),
        name="sello_update",
    ),
    path(
        "artista/eliminar/<int:pk>",
        login_required(ArtistaDelete.as_view()),
        name="artista_delete",
    ),
    path(
        "genero/eliminar/<int:pk>",
        login_required(GeneroDelete.as_view()),
        name="genero_delete",
    ),
    path(
        "sello/eliminar/<int:pk>",
        login_required(SelloDelete.as_view()),
        name="sello_delete",
    ),
]
