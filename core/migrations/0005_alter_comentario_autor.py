# Generated by Django 4.0 on 2021-12-20 22:30

import builtins
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('core', '0004_alter_artigo_autor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentario',
            name='autor',
            field=models.ForeignKey(on_delete=builtins.id, to='auth.user'),
        ),
    ]