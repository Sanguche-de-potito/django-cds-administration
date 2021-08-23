from django.db import models

# Create your models here.


class Artista(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return "{}".format(self.nombre)


class SelloDiscografico(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return "{}".format(self.nombre)


class GeneroMusical(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return "{}".format(self.nombre)
