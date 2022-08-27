from django.shortcuts import render,redirect
from Financeiro.models import Caixa
from Financeiro.forms import FormCaixa
from django.views.decorators.http import require_POST


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
    return render(request,'lista_lancamentos.html')

def altera_lancamentos(request):
    return render(request,'altera_lancamentos.html')

