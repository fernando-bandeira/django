# Generated by Django 4.0 on 2021-12-20 21:36

import builtins
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('conteudo', models.CharField(max_length=500, verbose_name='Conteúdo')),
                ('autor', models.CharField(max_length=50, verbose_name='Autor')),
                ('artigo', models.ForeignKey(on_delete=builtins.id, to='core.artigo')),
            ],
        ),
    ]
