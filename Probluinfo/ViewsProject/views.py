from datetime import datetime
from turtle import clear
import time,sys,os
from django.db import transaction
from datetime import datetime
from django.db import transaction
from django.http import HttpResponse
from django.shortcuts import render
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib import messages
from distutils.command.config import config
from http.client import HTTPResponse
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate
from Pessoas.models import Pessoas
from django.contrib.auth import login as login_django
from django.contrib.auth import logout 
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib.auth.forms import PasswordResetForm
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from Pessoas.models import Perfis
from Pessoas.forms import FormPessoasAltera
from Pessoas.models import Perfis
from Pessoas.forms import FormPessoasAltera


# Create your views here.

def efetua_paginacao(request, registros):
    paginacao = Paginator(registros,5)

    try:
        pagina = int(request.GET.get('pagina','1'))
    except ValueError:
        pagina = 1

    try:
        registros = paginacao.page(pagina)
    except (PageNotAnInteger, EmptyPage):
        registros = paginacao.page(1)
    return registros

def login(request):
    if request.user.is_authenticated:
        return redirect('base-pbi')
    else:                
        return render(request,'login.html')


def login_view(request):
        return render(request,'login.html')


def login_view(request):
        if request.method=='POST':
            login = request.POST.get('login')
            senha = request.POST.get('senha')
            user = authenticate(request, username=login, password=senha)
            if user is not None :
                if not user.id_perfil_id == 1 and request.POST.get('setor') != "pdv": # Verifica se o usuário é administrador
                    messages.warning(request,'🚫Login não permitido no módulo gestão!')
                else:
                    login_django(request,user)
                    if request.POST.get('setor')=="pdv":
                        request.session['base']="pdv"
                    else:
                        request.session['base']="gestao"
                    return redirect('base-pbi')
            if user == None:
                 messages.warning(request,'🚫Usuário ou Senha Inválidos!!!')
        return redirect('login')

def logout_view(request):
    logout(request)
    return render(request, 'logged_out.html')
        

def pagina_inexistente(request, *args, **argv):# precisa ser exception
    return render(request, 'pagina_inexistente.html',status=404)

def nao_autorizado(request, *args, **argv):  # precisa ser exception
    return render(request, 'nao_autorizado.html',status=401)

def erro_servidor(request, *args, **argv):
    return render(request, 'erro_servidor.html', status=500)

def suporte(request):
    if request.method == "POST":
        POST = request.POST
        try:
            send_mail('Contato via Sistema', f"Mensagem Enviada de {POST['nome']}\n{POST['mensagem']}" , 'pbisistema@hotmail.com' , ['leandroslv125@gmail.com'],fail_silently=False) 
            messages.success(request,'Contato enviado com Sucesso')
        except BadHeaderError:
            messages.warning(request,'Contato não Enviado!')
    return render(request, 'suporte.html')

def base_pbi(request):
    return render(request, 'base_pbi.html')


@transaction.atomic
def atualizar_dados(request):
    perfil = Perfis.objects.filter(is_active=True).order_by('descricao')
    pessoas = Pessoas.objects.filter(id=request.user.id)[0]
    data_nas = pessoas.dt_nascimento
    idade = datetime.now().year - data_nas.year
    data_nas = data_nas.strftime('%Y-%m-%d')
    if request.method == 'POST':
        form = FormPessoasAltera(request.POST, instance=pessoas)
        print(form.errors)
        if form.is_valid():
            print(form.cleaned_data)
            try:
                with transaction.atomic():
                    form.save()
                    messages.success(request, 'Alterado com sucesso!')
            except Exception as error:
                print(error)
    else:
        form = FormPessoasAltera()
    dados = {
                'perfis' : perfil,
                'pessoas' : pessoas,
                'data_nas': data_nas,
                'form': form,
                'idade' : idade
            }
    return render(request, 'atualizar_dados.html', dados)

def recup_senha(request):
    if request.method == "POST":
        password_reset_form = PasswordResetForm(request.POST)
        if password_reset_form.is_valid():
            data = password_reset_form.cleaned_data['email']
            associated_users = Pessoas.objects.filter(email=data)
            if associated_users.exists():
                token= default_token_generator.make_token(associated_users[0])
                uid = urlsafe_base64_encode(force_bytes(associated_users[0].pk))
                url= f"http://127.0.0.1:8000/reset/{uid}/{token}/"
                try:
                        send_mail('Resetar Senha', url, 'pbisistema@hotmail.com' , [associated_users[0].email], fail_silently=False)
                        messages.success(request,'Email enviado com Sucesso')
                except BadHeaderError:
                        messages.warning(request,'Email não Localizado!')

    return render(request, 'recup_senha.html')

def altera_senha(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Sua senha foi alterada')
            return render(request, 'altera_senha.html', {'form': form})
        else:
            messages.error(request, 'Verifique o alerta abaixo.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'altera_senha.html', {'form': form})


def sobre(request):
    return render(request, 'sobre.html')