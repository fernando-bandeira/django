# Generated by Django 4.0 on 2021-12-20 22:20

import builtins
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('core', '0003_alter_comentario_artigo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artigo',
            name='autor',
            field=models.ForeignKey(on_delete=builtins.id, to='auth.user'),
        ),
    ]