from django.contrib import admin
from .models import Actor

@admin.action(description='Pasar nombre UPPCASE')
def cambiar_nombre(modeladmin, request, queryset):
    for e in queryset:
        e.nombre=e.nombre.upper()
        e.save()

@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    actions = [cambiar_nombre]
    date_hierarchy = 'fecha_nacimiento'
    list_display = ["nombre","apellido","fecha_nacimiento"]
    ordering = ("nombre","apellido")




