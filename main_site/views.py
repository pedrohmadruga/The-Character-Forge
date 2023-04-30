from django.views.generic import TemplateView, ListView, DetailView
from . import models


class MainPageView(TemplateView):
    template_name = 'main_page.html'


class OriginalBuildsView(ListView):
    model = models.PersonagemOriginal
    template_name = 'original_builds.html'
    context_object_name = 'personagens'
    paginate_by = 3


class PersonagemOriginalDetailView(DetailView):
    model = models.PersonagemOriginal
    template_name = 'original_character_detail.html'
    context_object_name = 'personagem'
