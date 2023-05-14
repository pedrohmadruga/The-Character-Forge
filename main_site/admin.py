from django.contrib import admin
from main_site import models


@admin.register(models.PersonagemOriginal)
class PersonagemOriginalAdmin(admin.ModelAdmin):
    list_display = ('nome', 'raca', 'classe',)