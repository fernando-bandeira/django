from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import user_passes_test
from .models import Artigo, Comentario


def index(request):
    context = {
        'artigos': Artigo.objects.order_by('-id')
    }
    return render(request, 'index.html', context)


def artigo(request, pk):
    if request.method == 'POST':
        autor = User.objects.all().get(id=request.POST.get('autor'))
        coment = request.POST.get('coment')
        Comentario(conteudo=coment, autor=autor, artigo=pk).save()
    context = {
        'artigo': Artigo.objects.get(id=pk),
        'comentarios': Comentario.objects.filter(artigo=pk).order_by('-id')
    }
    return render(request, 'artigo.html', context)


@user_passes_test(lambda u: u.is_superuser, login_url='/')
def criar_artigo(request):
    if request.method == 'POST':
        autor = User.objects.get(id=request.POST.get('autor'))
        titulo = request.POST.get('titulo')
        conteudo = request.POST.get('conteudo')
        artigo = Artigo(titulo=titulo, conteudo=conteudo, autor=autor)
        artigo.save()
        return redirect(f'/artigo/{artigo.id}')

    return render(request, 'criar_artigo.html')
