# Generated by Django 4.2 on 2023-04-11 02:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_site', '0005_personagemoriginalmodel_backstory_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='PersonagemOriginalModel',
            new_name='PersonagemModel',
        ),
    ]