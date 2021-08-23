from django.db import models
from maintenance.models import Artista, SelloDiscografico, GeneroMusical

# Create your models here.


class Album(models.Model):
    nombre = models.CharField(max_length=1000)
    año = models.IntegerField()
    artista = models.ForeignKey(
        Artista, null=False, blank=False, on_delete=models.CASCADE
    )
    sello = models.ForeignKey(
        SelloDiscografico, null=False, blank=False, on_delete=models.CASCADE
    )
    genero = models.ForeignKey(
        GeneroMusical, null=False, blank=False, on_delete=models.CASCADE
    )

    def __str__(self):
        return "{}".format(self.nombre)
