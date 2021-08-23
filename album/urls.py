from django.contrib import admin
from django.urls import path
from album.views import AlbumList, AlbumCreate, AlbumUpdate, AlbumDelete, about_page
from django.contrib.auth.decorators import login_required

app_name = "album"

urlpatterns = [
    path("list/", login_required(AlbumList.as_view()), name="album_list"),
    path("create/", login_required(AlbumCreate.as_view()), name="album_create"),
    path(
        "editar/<int:pk>/", login_required(AlbumUpdate.as_view()), name="album_update"
    ),
    path(
        "eliminar/<int:pk>", login_required(AlbumDelete.as_view()), name="album_delete"
    ),
    path("about/", login_required(about_page), name="about"),
]
