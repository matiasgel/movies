from django.db import models
from movie_database.models import Actor


class Pelicula(models.Model):
    nombre = models.CharField(max_length=200)
    resenia = models.TextField(max_length=1500)
    actores =  models.ManyToManyField(Actor)
    foto = models.ImageField(upload_to='pelicula')

