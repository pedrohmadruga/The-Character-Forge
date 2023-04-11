from django.contrib import admin
from main_site import models


@admin.register(models.PersonagemModel)
class PersonagemOriginalAdmin(admin.ModelAdmin):
    list_display = ('nome', 'raca', 'classe',)


@admin.register(models.Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('nome', )


