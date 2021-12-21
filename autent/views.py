from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required, user_passes_test


@user_passes_test(lambda u: not u.is_authenticated, login_url='/')
def cadastro(request):
    if request.method == 'POST':
        campos = request.POST

        if not all(campos.values()):
            messages.error(request, 'Preencha todos os campos.')
            return render(request, 'cadastro.html')
        if campos.get('senha1') != campos.get('senha2'):
            messages.error(request, 'Senhas não conferem.')
            return render(request, 'cadastro.html')
        if User.objects.filter(username=campos.get('user')).exists():
            messages.error(request, 'Nome de usuário já existe.')
            return render(request, 'cadastro.html')
        if User.objects.filter(email=campos.get('email')).exists():
            messages.error(request, 'E-mail já existe.')
            return render(request, 'cadastro.html')

        nome = campos.get('nome').split()

        User.objects.create_user(
            username=campos.get('user'),
            password=campos.get('senha1'),
            first_name=nome[0],
            last_name=nome[-1] if len(nome) else '',
            email=campos.get('email')
        ).save()
        messages.success(request, 'Cadastro realizado com sucesso!')
        return redirect('entrar')


    return render(request, 'cadastro.html')


@user_passes_test(lambda u: not u.is_authenticated, login_url='/')
def entrar(request):
    if request.method == 'POST':
        campos = request.POST
        user = auth.authenticate(
            request,
            username=campos.get('user'),
            password=campos.get('senha')
        )
        if user is None:
            messages.error(request, 'Credenciais inválidas.')
        else:
            auth.login(request, user)
            messages.success(request, 'Você foi autenticado com sucesso.')
            return redirect('/')

    return render(request, 'entrar.html')


@login_required(login_url='/')
def sair(request):
    auth.logout(request)
    return redirect('/')
