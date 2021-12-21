from django.urls import path
from .views import cadastro, entrar, sair

urlpatterns = [
    path('', entrar),
    path('cadastro/', cadastro, name='cadastro'),
    path('entrar/', entrar, name='entrar'),
    path('sair/', sair, name='sair')
]
