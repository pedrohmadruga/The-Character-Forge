# Generated by Django 4.2 on 2023-05-14 19:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_site', '0009_personagemoriginal_nivel_0'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='personagemoriginal',
            name='tags',
        ),
        migrations.DeleteModel(
            name='Tag',
        ),
    ]