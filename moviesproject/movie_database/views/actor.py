from django.views.generic import TemplateView
from movie_database import models


class ActoresView(TemplateView):
    template_name = "actores.html"
    def get_context_data(self,**kwargs):
        context = super().get_context_data(** kwargs)
        context["actores"]=models.Actor.objects.all()
        return context

