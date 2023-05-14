from django.views.generic import TemplateView, ListView, DetailView
from . import models
from django.db.models import Q


class MainPageView(TemplateView):
    template_name = 'main_page.html'


class OriginalBuildsView(ListView):
    model = models.PersonagemOriginal
    template_name = 'original_builds.html'
    context_object_name = 'personagens'
    paginate_by = 5

    def get_queryset(self):
        queryset = super().get_queryset()

        name = self.request.GET.get('name')
        race = self.request.GET.get('race')
        classe = self.request.GET.get('class')

        if name or race or classe:
            queryset = queryset.filter(
                Q(nome__icontains=name) if name else Q(),
                Q(raca__icontains=race) if race else Q(),
                Q(classe__icontains=classe) if classe else Q()
            )

        return queryset


class PersonagemOriginalDetailView(DetailView):
    model = models.PersonagemOriginal
    template_name = 'original_character_detail.html'
    context_object_name = 'personagem'
