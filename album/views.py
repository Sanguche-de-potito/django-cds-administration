from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from album.models import Album
from album.forms import AlbumForm
from django.urls import reverse_lazy


# Create your views here.


class AlbumList(ListView):
    model = Album
    template_name = "album/album_list.html"
    paginate_by = 9


class AlbumCreate(CreateView):
    model = Album
    form_class = AlbumForm
    template_name = "album/album_form.html"
    success_url = reverse_lazy("album:album_list")


class AlbumUpdate(UpdateView):
    model = Album
    form_class = AlbumForm
    template_name = "album/album_form.html"
    success_url = reverse_lazy("album:album_list")


class AlbumDelete(DeleteView):
    model = Album
    template_name = "album/album_delete.html"
    success_url = reverse_lazy("album:album_list")


def about_page(request):
    return render(request, "about.html")
