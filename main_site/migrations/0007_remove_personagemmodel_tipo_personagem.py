# Generated by Django 4.2 on 2023-04-11 02:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_site', '0006_rename_personagemoriginalmodel_personagemmodel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='personagemmodel',
            name='tipo_personagem',
        ),
    ]