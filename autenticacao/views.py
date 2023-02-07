from django.shortcuts import render, get_object_or_404
# from django.http import HttpResponse
from .utils import password_is_valid, email_html
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib import messages, auth
from django.contrib.messages import constants
import os
from django.conf import settings
from .models import Ativacao
from hashlib import sha256
from django.core.mail import send_mail


def cadastro(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect('/')
        senha_erro = request.GET.get("senha_erro")
        return render(request, 'cadastro.html', {"senha": senha_erro})
    elif request.method == "POST":
        username = request.POST.get('usuario')
        senha = request.POST.get('senha')
        email = request.POST.get('email')
        confirma_senha = request.POST.get('confirmar-senha')

        
        error_codes = [1, 2, 3, 4, 5]
        result = password_is_valid(request, senha, confirma_senha)

        if result != 6:
            for error_code in error_codes:
                if result == error_code:
                    return redirect(f'/auth/cadastro/?senha_erro={error_code}')

        # if  password_is_valid(request, senha, confirma_senha) != 6:
        #     if password_is_valid(request, senha, confirma_senha) == 1:
        #         return redirect('/auth/cadastro/?senha_erro=1')
        #     if password_is_valid(request, senha, confirma_senha) == 2:
        #         return redirect('/auth/cadastro/?senha_erro=2')
        #     if password_is_valid(request, senha, confirma_senha) == 3:
        #         return redirect('/auth/cadastro/?senha_erro=3')
        #     if password_is_valid(request, senha, confirma_senha) == 4:
        #         return redirect('/auth/cadastro/?senha_erro=4')
        #     if password_is_valid(request, senha, confirma_senha) == 5:
        #         return redirect('/auth/cadastro/?senha_erro=5')

        # Vai tirar todos os espaços strip()
        if len(username.strip()) == 0 or len(email.strip()) == 0:
            messages.add_message(request, constants.ERROR, 'E-mail ou Senha não podem ficar vazior')
            return redirect('/auth/cadastro/')

        # Verificar se já existe email
        if User.objects.filter(email=email).exists():
            messages.add_message(request, constants.WARNING, 'Já existe um usuário com esse e-mail')
            return redirect('/auth/cadastro/')

        # Verificar se já existe nome igual
        if User.objects.filter(username=username).exists():
            messages.add_message(request, constants.WARNING, 'Já existe um usuário com esse nome')
            return redirect('/auth/cadastro/')

        try:
            user = User.objects.create_user(username=username,
                                            email=email,
                                            password=senha,
                                            is_active=False)
            user.save()

            token = sha256(f"{username}{email}".encode()).hexdigest()
            ativacao = Ativacao(token=token, user=user)
            ativacao.save()

            path_template = os.path.join(settings.BASE_DIR, 'autenticacao/templates/emails/cadastro_confirmado.html')
            email_html(path_template, 'Cadastro confirmado', [email, ], username=username, link_ativacao=f"127.0.0.1:8000/auth/ativar_conta/{token}")

            messages.add_message(request, constants.SUCCESS, 'Verifique sua caixa de e-mail.')

            return redirect('/auth/logar')

        except:
            messages.add_message(request, constants.ERROR, 'Erro Interno no sistema')
            return redirect('/auth/cadastro')


def logar(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect('/')
        return render(request, 'logar.html')
    elif request.method == "POST":
        username = request.POST.get('usuario')
        senha = request.POST.get('senha')

        usuario = auth.authenticate(username=username, password=senha)

        if not usuario:
            messages.add_message(request, constants.WARNING, 'Username ou senha inválidos')
            return redirect('/auth/logar')
        else:
            auth.login(request, usuario)
            return redirect('/pacientes')


def sair(request):
    auth.logout(request)
    return redirect('/auth/logar')


def ativar_conta(request, token):
    token = get_object_or_404(Ativacao, token=token)
    if token.ativo:
        messages.add_message(request, constants.WARNING, 'Essa token já foi usado')
        return redirect('/auth/logar')
    user = User.objects.get(username=token.user.username)
    user.is_active = True
    user.save()
    token.ativo = True
    token.save()
    # send_mail('Assunto', 'Esse é o email que estou te enviando', 'pedr.compras@gmail.com',['henri-17@live.com'])
    messages.add_message(request, constants.SUCCESS, 'Conta ativa com sucesso')
    return redirect('/auth/logar')
