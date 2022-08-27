from datetime import datetime
from django.shortcuts import render, redirect
from django.db import transaction
from django.contrib.auth.hashers import make_password
from django.contrib import messages

from Pessoas.models import Pessoas, Perfis
from Pessoas.forms import FormPessoas, FormPessoasAltera
from ViewsProject.views import efetua_paginacao

# Create your views here.
@transaction.atomic
def cadastra_pessoas(request):
    perfil = Perfis.objects.filter(is_active=True).order_by('descricao')

    if request.method == 'POST':
        formPessoa = FormPessoas(request.POST or None)
        if formPessoa.is_valid():
            try:
                with transaction.atomic():
                    formPessoa.cleaned_data['password'] = make_password(formPessoa.cleaned_data['password'])
                    Pessoas.objects.create(**formPessoa.cleaned_data)
                    messages.success(request, 'Cadastrado com sucesso!')
            except Exception as error:
                print(error)
            return redirect(lista_pessoas)
    else:
        formPessoa = FormPessoas()
    print(formPessoa.errors)

    dados = {
                'perfis' : perfil,
            }
    return render(request,'cadastra_pessoas.html', dados)

def lista_pessoas(request):
    procura = request.GET.get('procura')
    
    if procura:
        tipoPessoa = Pessoas.objects.filter(first_name__icontains=procura)
    else:
        tipoPessoa = Pessoas.objects.all()

    total = tipoPessoa.count

    dados = {
                'tipos' : tipoPessoa,
                'total' : total, 
                'procura' : procura,
                'porPagina' : efetua_paginacao(request, tipoPessoa)
            }
    return render(request, 'lista_pessoas.html', dados)

@transaction.atomic
def altera_pessoas(request,id):
    perfil = Perfis.objects.filter(is_active=True).order_by('descricao')
    pessoas = Pessoas.objects.get(id=id)
    data_nas = pessoas.dt_nascimento
    idade = datetime.now().year - data_nas.year
    data_nas = data_nas.strftime('%Y-%m-%d')
    if request.method == 'POST':
        form = FormPessoasAltera(request.POST, instance=pessoas)
        if form.is_valid():
            print(form.cleaned_data)
            try:
                with transaction.atomic():
                    form.save()
            except Exception as error:
                print(error)
            return redirect(lista_pessoas)
    else:
        form = FormPessoasAltera()
    dados = {
                'perfis' : perfil,
                'pessoas' : pessoas,
                'data_nas': data_nas,
                'form': form,
                'idade' : idade
            }
    return render(request, 'altera_pessoas.html', dados)
   
