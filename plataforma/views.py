from django.shortcuts import render, redirect, get_object_or_404
import os
from datetime import datetime
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.messages import constants
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from PIL import Image
from fpdf import FPDF
from autenticacao.models import Ativacao
from .models import Pacientes, DadosPaciente, Refeicao, Opcao


# from django.generic.views import render


@login_required(login_url='/auth/logar/')
def pacientes(request):
    if request.method == "GET":
        pacientes = Pacientes.objects.filter(nutri=request.user)
        return render(request, 'pacientes.html', {'pacientes': pacientes})
    elif request.method == "POST":
        perfil = request.FILES.get('perfil')
        nome = request.POST.get('nome')
        sexo = request.POST.get('sexo')
        idade = request.POST.get('idade')
        email = request.POST.get('email')
        telefone = request.POST.get('telefone')

        if (len(nome.strip()) == 0) or (len(sexo.strip()) == 0) or (len(idade.strip()) == 0) or (
                len(email.strip()) == 0) or (len(telefone.strip()) == 0):
            messages.add_message(request, constants.ERROR, 'Preencha todos os campos')
            return redirect('/pacientes/')

        if not idade.isnumeric():
            messages.add_message(request, constants.WARNING, 'Digite uma idade válida')
            return redirect('/pacientes/')

        paciente = Pacientes.objects.filter(email=email)

        if paciente.exists():
            messages.add_message(request, constants.INFO, 'Já existe um paciente com esse E-mail')
            return redirect('/pacientes/')

        try:
            paciente = Pacientes(perfil=perfil,
                                 nome=nome,
                                 sexo=sexo,
                                 idade=idade,
                                 email=email,
                                 telefone=telefone,
                                 nutri=request.user)

            paciente.save()

            messages.add_message(request, constants.SUCCESS, 'Paciênte cadastrado com sucesso')
            return redirect('/pacientes/')
        except:
            messages.add_message(request, constants.ERROR, 'Erro interno do sistema')
            return redirect('/pacientes/')


@login_required(login_url='/auth/logar/')
def dados_paciente_listar(request):
    if request.method == "GET":
        pacientes = Pacientes.objects.filter(nutri=request.user)
        return render(request, 'dados_paciente_listar.html', {'pacientes': pacientes})


@login_required(login_url='/auth/logar/')
def dados_paciente(request, id):
    paciente = get_object_or_404(Pacientes, id=id)
    if not paciente.nutri == request.user:
        messages.add_message(request, constants.DEBUG, 'Esse paciente não é seu')
        return redirect('/dados_paciente/')

    if request.method == "GET":
        dados_paciente = DadosPaciente.objects.filter(paciente=paciente)
        return render(request, 'dados_paciente.html', {'paciente': paciente, 'dados_paciente': dados_paciente})

    if request.method == "GET":
        return render(request, 'dados_paciente.html', {'paciente': paciente})
    elif request.method == "POST":
        peso = request.POST.get('peso')
        altura = request.POST.get('altura')
        gordura = request.POST.get('gordura')
        musculo = request.POST.get('musculo')

        hdl = request.POST.get('hdl')
        ldl = request.POST.get('ldl')
        colesterol_total = request.POST.get('ctotal')
        triglicerídios = request.POST.get('triglicerídios')

        if (len(peso.strip()) == 0) or (len(altura.strip()) == 0) or (len(gordura.strip()) == 0) or (
                len(musculo.strip()) == 0) or (len(hdl.strip()) == 0) or (len(ldl.strip()) == 0) or (
                len(colesterol_total.strip()) == 0) or (len(triglicerídios.strip()) == 0):
            messages.add_message(request, constants.ERROR, 'Preencha todos os campos')
            return redirect('/dados_paciente/')

        paciente = DadosPaciente(paciente=paciente,
                                 data=datetime.now(),
                                 peso=peso,
                                 altura=altura,
                                 percentual_gordura=gordura,
                                 percentual_musculo=musculo,
                                 colesterol_hdl=hdl,
                                 colesterol_ldl=ldl,
                                 colesterol_total=colesterol_total,
                                 trigliceridios=triglicerídios)

        paciente.save()

        messages.add_message(request, constants.SUCCESS, 'Dados cadastrado com sucesso')

        return redirect(f'/dados_paciente/{id}')


@login_required(login_url='/auth/logar/')
@csrf_exempt
def grafico_peso(request, id):
    paciente = Pacientes.objects.get(id=id)
    dados = DadosPaciente.objects.filter(paciente=paciente).order_by("data")

    pesos = [dado.peso for dado in dados]
    labels = [dado.data for dado in dados]
    data = {'peso': pesos,
            'labels': labels}
    return JsonResponse(data)


def plano_alimentar_listar(request):
    if request.method == "GET":
        pacientes = Pacientes.objects.filter(nutri=request.user)
        return render(request, 'plano_alimentar_listar.html', {'pacientes': pacientes})


def plano_alimentar(request, id):
    paciente = get_object_or_404(Pacientes, id=id)
    if not paciente.nutri == request.user:
        messages.add_message(request, constants.ERROR, 'Esse paciente não é seu')
        return redirect('/dados_paciente/')

    if request.method == "GET":
        r1 = Refeicao.objects.filter(paciente=paciente).order_by("horario")
        opcao = Opcao.objects.all()
        return render(request, 'plano_alimentar.html', {'paciente': paciente, 'refeicao': r1, 'opcao': opcao})


def refeicao(request, id_paciente):
    paciente = get_object_or_404(Pacientes, id=id_paciente)
    if not paciente.nutri == request.user:
        messages.add_message(request, constants.ERROR, 'Esse paciente não é seu')
        return redirect('/dados_paciente/')

    if request.method == "POST":
        titulo = request.POST.get('titulo')
        horario = request.POST.get('horario')
        carboidratos = request.POST.get('carboidratos')
        proteinas = request.POST.get('proteinas')
        gorduras = request.POST.get('gorduras')

        r1 = Refeicao(paciente=paciente,
                      titulo=titulo,
                      horario=horario,
                      carboidratos=carboidratos,
                      proteinas=proteinas,
                      gorduras=gorduras)

        r1.save()

        messages.add_message(request, constants.SUCCESS, 'Refeição cadastrada')
        return redirect(f'/plano_alimentar/{id_paciente}')


def opcao(request, id_paciente):
    if request.method == "POST":
        id_refeicao = request.POST.get('refeicao')
        imagem = request.FILES.get('imagem')
        descricao = request.POST.get("descricao")

        o1 = Opcao(refeicao_id=id_refeicao,
                   imagem=imagem,
                   descricao=descricao)

        o1.save()

        messages.add_message(request, constants.SUCCESS, 'Opção cadastrada')
        return redirect(f'/plano_alimentar/{id_paciente}')


@login_required(login_url='/auth/logar/')
def gera_pdf(request, id_paciente):

     # aqui você pode recuperar as informações do paciente, opções, usuário etc.
    pacientes = Pacientes.objects.get(id=int(id_paciente))
    refeicaos = Refeicao.objects.filter(paciente=pacientes)
    opcaos = Opcao.objects.all()
    dados_paciente = DadosPaciente.objects.filter(paciente=pacientes)

    #Crie uma instância da classe FPDF
    pdf = FPDF('P', 'mm', 'A4')
    #Adicione uma página ao PDF
    pdf.add_page()
    # Defina o tipo de fonte e tamanho que será utilizado
    pdf.set_font('Times', 'B', 16)

    # Adicione texto ao PDF
   
    # pdf.cell(35,10, 'Nutricionista:'1,0,'L',1)
   
    pdf.text(80, 8, f'Nutricionista {pacientes.nutri}')
    pdf.set_font('helvetica', 'BI', size=12)
    pdf.set_fill_color(9, 121, 101)
    foto_paciete = os.path.join(settings.BASE_DIR, pacientes.perfil.url[1::])
    pdf.image(foto_paciete, x = 11, y = 13, w = 30, h = 30)
    pdf.multi_cell(100, 6,         f'\n                               Nome: {pacientes.nome}\n                               '
                            f'Idade: {pacientes.idade} anos\n                               '
                            f'Email: {pacientes.email}\n                               '
                            f'Telefone: {pacientes.telefone}\n                               ')
    
    
    
    # Adicione imagens ao PDF
    # image = os.path.join(settings.MEDIA_ROOT, 'opcao/almoco.jpeg')
    # pdf.image(f'{opcao.imagem}', 30, 60)
    
    pdf.cell(0,10, ' Refeições: ', 1, 1, 'C', 1)
    for opcao in opcaos:
        
        pdf. cell(0,10, f'  {opcao.refeicao}:',1,1,'L',1)
        pdf. cell(1,10, f' -> {opcao.descricao}',1,1,'L',0)
    
    # for refeicao in refeicaos:
    #       pdf.text(wd,al,f'\n({refeicao.horario})' )   
    #       al += 20
    
    # alt = 60
    # wid = 15
    # foto_descricao = os.path.join(settings.BASE_DIR, opcaos.imagem.url[1::])
    # print(foto_descricao)
    # pdf.image(foto_descricao, x = 20, y = 70, w = 30, h = 30)
    # wd= 25
    # hg = 72
    # for opcao in  opcaos:
    #     pdf.text(80, 50, '---REFEIÇÕES---') 
    #     pdf.text(wid,alt,'________________________________________________________________________')
    #     pdf.text(wid,alt,f'{opcao.refeicao}' )       
    #     pdf.text(wd, hg, f'{opcao.descricao}')
    #     hg += 20
    #     alt += 20
        
    pdf.cell(0,10, ' Dados do Paciente: ', 1, 1, 'C', 1)
    for dado in dados_paciente:
        pdf.cell(1,10, f' Data: {dado.data}',1,1,'L',0)
        pdf.cell(1,10, f' Altura: {dado.altura}m',1,1,'L',1)
        pdf.cell(1,10, f' Peso: {dado.peso}Kg',1,2,'L',1)       
                
    
    # pdf.multi_cell (150, 5, f'\n                               Altura: {dados_paciente.altura}m\n                               '
    #                         f'Peso: {dados_paciente.peso}kg\n                               '
    #                         f'Porcentual de Gordura: {dados_paciente.percentual_gordura}%\n                               '
    #                         f'Percentual de Musculos: {dados_paciente.percentual_musculo}%\n                               ')
        


    # Defina o caminho onde o PDF será salvo
    caminho_pdf = os.path.join(settings.MEDIA_ROOT, f'pdf/{pacientes.nome}.pdf')
    # Gere o PDF
    pdf.output(caminho_pdf)
    # Retorne o arquivo gerado
    return redirect(f'/media/pdf/{pacientes.nome}.pdf')


  
