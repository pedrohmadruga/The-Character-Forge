# Generated by Django 4.2 on 2023-04-30 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_site', '0008_rename_personagemmodel_personagemoriginal'),
    ]

    operations = [
        migrations.AddField(
            model_name='personagemoriginal',
            name='nivel_0',
            field=models.TextField(default=''),
        ),
    ]