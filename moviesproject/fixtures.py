from movie_database import models
import datetime
from django.conf import  settings
path_imagen=settings.MEDIA_ROOT+"/actor/foto1.jpg"
for x in range(100):
  actor=models.Actor(nombre="actor"+str(x),
                     apellido="apellido"+str(x),
                     fecha_nacimiento=datetime.date(1978,2,1),
                     bio="ksdjl aoidasj dklsajdlkas jdlkja asdj asjl kjasdlk as as d ajsd askl dasjd as lasd asjlksadj laj"
                     )
  actor.save()

