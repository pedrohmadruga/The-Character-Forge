# Generated by Django 4.2 on 2023-04-30 17:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_site', '0007_remove_personagemmodel_tipo_personagem'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='PersonagemModel',
            new_name='PersonagemOriginal',
        ),
    ]