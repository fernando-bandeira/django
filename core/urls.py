from django.urls import path
from .views import criar_artigo, index, artigo

urlpatterns = [
    path('', index, name='index'),
    path('artigo/<int:pk>', artigo, name='artigo'),
    path('criar_artigo/', criar_artigo, name='criar_artigo')
]
