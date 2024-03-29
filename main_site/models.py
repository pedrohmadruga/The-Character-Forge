from django.db import models


class PersonagemBase(models.Model):
    nome = models.CharField(max_length=100, default='')
    raca = models.CharField(max_length=50, default='')
    classe = models.CharField(max_length=100, default='')
    image = models.ImageField(upload_to='media/', blank=True)
    descricao = models.TextField(max_length=250, default='')
    backstory = models.TextField(default='')
    nivel_0 = models.TextField(default='')
    nivel_1 = models.TextField(default='')
    nivel_2 = models.TextField(default='')
    nivel_3 = models.TextField(default='')
    nivel_4 = models.TextField(default='')
    nivel_5 = models.TextField(default='')
    nivel_6 = models.TextField(default='')
    nivel_7 = models.TextField(default='')
    nivel_8 = models.TextField(default='')
    nivel_9 = models.TextField(default='')
    nivel_10 = models.TextField(default='')
    nivel_11 = models.TextField(default='')
    nivel_12 = models.TextField(default='')
    nivel_13 = models.TextField(default='')
    nivel_14 = models.TextField(default='')
    nivel_15 = models.TextField(default='')
    nivel_16 = models.TextField(default='')
    nivel_17 = models.TextField(default='')
    nivel_18 = models.TextField(default='')
    nivel_19 = models.TextField(default='')
    nivel_20 = models.TextField(default='')
    ponto_positivo = models.TextField(default='')
    ponto_negativo = models.TextField(default='')


class PersonagemOriginal(PersonagemBase):
    personagembase_ptr = models.OneToOneField(
        PersonagemBase,
        parent_link=True,
        on_delete=models.CASCADE,
        primary_key=True
    )

    def __str__(self):
        return self.nome

class PersonagemRecriado(PersonagemBase):
    personagembase_ptr = models.OneToOneField(
        PersonagemBase,
        parent_link=True,
        on_delete=models.CASCADE,
        primary_key=True
    )

    def __str__(self):
        return self.nome
