from django.shortcuts import render,redirect
from Financeiro.models import Caixa
from Financeiro.forms import FormCaixa
from django.db import transaction
from django.views.decorators.http import require_POST
from ViewsProject.views import efetua_paginacao


# Create your views here.
def cadastra_lancamentos(request):
    tipo = Caixa.TIPOS_CHOICES
    if request.method == 'POST':
        form = FormCaixa(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect(cadastra_lancamentos)
    dados = {
        'tipo':tipo,
    }
    return render(request,'cadastra_lancamentos.html',dados)

def lista_lancamentos(request):
    procura = request.GET.get('procura')
    
    if procura:
        tipo = Caixa.objects.filter(first_name__icontains=procura)
    else:
        tipo = Caixa.objects.all()

    total = tipo.count

    dados = {
                'tipos' : tipo,
                'total' : total, 
                'procura' : procura,
                'porPagina' : efetua_paginacao(request, tipo)
            }
    return render(request,'lista_lancamentos.html', dados)

def altera_lancamentos(request):
    tipo = Caixa.objects.filter(is_active=True).order_by('descricao')
    caixa = Caixa.objects.get(id=id)
    data_lan = caixa.dt_lancamento
    data_lan = data_lan.strftime('%Y-%m-%d')
    if request.method == 'POST':
        form = FormCaixa(request.POST, instance=caixa)
        if form.is_valid():
            print(form.cleaned_data)
            try:
                with transaction.atomic():
                    form.save()
            except Exception as error:
                print(error)
            return redirect(lista_lancamentos)
    else:
        form = FormCaixa()
    dados = {
                'tipo' : tipo,
                'caixa' : caixa,
                'data_lan': data_lan,
                'form': form,
              
            }

    return render(request,'altera_lancamentos.html' , dados)

