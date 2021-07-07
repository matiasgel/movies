from django.db import models

class Actor(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    fecha_nacimiento=models.DateField()
    bio = models.TextField(max_length=1500)
    foto = models.ImageField(upload_to='actor')
    def __str__(self):
        return self.nombre+" "+self.apellido



