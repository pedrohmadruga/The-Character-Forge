from django.views.generic import TemplateView, ListView, DetailView
from . import models


class MainPageView(TemplateView):
    template_name = 'main_page.html'


class OriginalBuildsView(ListView):
    model = models.PersonagemModel
    template_name = 'original_builds.html'
    context_object_name = 'personagens'
    paginate_by = 5


class PersonagemOriginalDetailView(DetailView):
    model = models.PersonagemModel
    template_name = 'character_detail.html'
    context_object_name = 'personagem'
