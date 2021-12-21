from django.db import models
from django.contrib.auth.models import User

class Artigo(models.Model):
    titulo = models.CharField('Título', max_length=100)
    conteudo = models.CharField('Conteúdo', max_length=500)
    autor = models.ForeignKey(User, id)

class Comentario(models.Model):
    conteudo = models.CharField('Conteúdo', max_length=500)
    autor = models.ForeignKey(User, id)
    artigo = models.IntegerField('Artigo')
