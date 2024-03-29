# Generated by Django 4.2 on 2023-08-16 23:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PersonagemBase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(default='', max_length=100)),
                ('raca', models.CharField(default='', max_length=50)),
                ('classe', models.CharField(default='', max_length=100)),
                ('image', models.ImageField(blank=True, upload_to='media/')),
                ('descricao', models.TextField(default='', max_length=250)),
                ('backstory', models.TextField(default='')),
                ('nivel_0', models.TextField(default='')),
                ('nivel_1', models.TextField(default='')),
                ('nivel_2', models.TextField(default='')),
                ('nivel_3', models.TextField(default='')),
                ('nivel_4', models.TextField(default='')),
                ('nivel_5', models.TextField(default='')),
                ('nivel_6', models.TextField(default='')),
                ('nivel_7', models.TextField(default='')),
                ('nivel_8', models.TextField(default='')),
                ('nivel_9', models.TextField(default='')),
                ('nivel_10', models.TextField(default='')),
                ('nivel_11', models.TextField(default='')),
                ('nivel_12', models.TextField(default='')),
                ('nivel_13', models.TextField(default='')),
                ('nivel_14', models.TextField(default='')),
                ('nivel_15', models.TextField(default='')),
                ('nivel_16', models.TextField(default='')),
                ('nivel_17', models.TextField(default='')),
                ('nivel_18', models.TextField(default='')),
                ('nivel_19', models.TextField(default='')),
                ('nivel_20', models.TextField(default='')),
                ('ponto_positivo', models.TextField(default='')),
                ('ponto_negativo', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='PersonagemOriginal',
            fields=[
                ('personagembase_ptr', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='main_site.personagembase')),
            ],
            bases=('main_site.personagembase',),
        ),
        migrations.CreateModel(
            name='PersonagemRecriado',
            fields=[
                ('personagembase_ptr', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='main_site.personagembase')),
            ],
            bases=('main_site.personagembase',),
        ),
    ]
