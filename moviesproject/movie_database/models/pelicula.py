from django.db import models
from movie_database.models import Actor
from django.contrib import admin


class Pelicula(models.Model):
    nombre = models.CharField(max_length=200)
    resenia = models.TextField(max_length=1500)
    actores =  models.ManyToManyField(Actor)
    foto = models.ImageField(upload_to='pelicula')
    def __str__(self):
        return self.nombre

@admin.register(Pelicula)
class PeliculaAdmin(admin.ModelAdmin):
    list_filter = ("nombre",)
    filter_horizontal = ("actores",)

