from django.shortcuts import render,redirect
from django.views.decorators.http import require_POST
from django.db import transaction
from django.contrib import messages

from Cursos.forms import FormCursos,FormMatriculas,FormNotas,FormSalas
from Cursos.models import Matriculas,Cursos,Salas
from ViewsProject.views import efetua_paginacao

# Create your views here.
def cadastra_cursos(request):
    if request.method == 'POST':
        form = FormCursos(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cadastrado com sucesso!')
    return render(request,'cadastra_cursos.html')
    
def cadastra_matriculas(request):
    periodos = Matriculas.PERIODOS_CHOICES
    if request.method == 'POST':
        form = FormMatriculas(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect(cadastra_matriculas)

    dados = {
                'periodos': periodos,
            }
    return render(request,'cadastra_matriculas.html', dados)

def cadastra_salas(request):
    if request.method == 'POST':
        form = FormSalas(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cadastrado com sucesso!')
    return render(request,'cadastra_salas.html')

def cadastra_notas(request):
    if request.method == 'POST':
        form = FormNotas(request.POST or None)
        if form.is_valid():
            form.save()
    return render(request,'cadastra_notas.html')

def lista_cursos(request):
    procura= request.GET.get('procura')

    if procura:
        cursos = Cursos.objects.filter(nm_curso__icontains=procura)
    else:
        cursos = Cursos.objects.all()
    
    total = cursos.count

    dados = {
                'cursos' : cursos,
                'total' : total, 
                'procura' : procura,
                'porPagina' : efetua_paginacao(request, cursos)
            }
    return render(request,'lista_cursos.html',dados)

def lista_matriculas(request):
    procura = request.GET.get('procura')

    if procura:
        matricula = Matriculas.objects.filter(nome__icontains=procura)|Matriculas.objects.filter(email__icontains=procura)
    else:
        matricula = Matriculas.objects.all()

    total = matricula.count

    dados = {
                'matricula' : matricula, 
                'total' : total, 
                'procura' : procura,
            }
    return render(request, 'lista_matriculas.html', dados)

def lista_notas(request):
    return render(request,'lista_notas.html')

def lista_salas(request):
    procura= request.GET.get('procura')
    
    if procura:
        salas = Salas.objects.filter(nm_sala__icontains=procura)
    else:
        salas = Salas.objects.all()
    
    total = salas.count

    dados = {
                'salas' : salas,
                'total' : total, 
                'procura' : procura,
                'porPagina' : efetua_paginacao(request, salas)
            }

    return render(request,'lista_salas.html',dados)

@transaction.atomic
def altera_cursos(request,id):
    cursos = Cursos.objects.get(id=id)
    if request.method == 'POST':
        form = FormCursos(request.POST,instance=cursos)
        if form.is_valid():
            print(form.cleaned_data)
            try:
                with transaction.atomic():
                    form.save()
            except Exception as error:
                print(error)
            return redirect(lista_cursos)
    else:
        form = FormCursos()
    dados = {
                'cursos' : cursos,
            }
    return render(request,'altera_cursos.html', dados)

def altera_matriculas(request):
    return render(request,'altera_matriculas.html')

def altera_notas(request):
    return render(request,'altera_notas.html')

@transaction.atomic
def altera_salas(request,id):
    salas = Salas.objects.get(id=id)
    if request.method == 'POST':
        form = FormSalas(request.POST,instance=salas)
        if form.is_valid():
            print(form.cleaned_data)
            try:
                with transaction.atomic():
                    form.save()
            except Exception as error:
                print(error)
            return redirect(lista_salas)
    else:
        form = FormSalas()
    dados = {
                'salas' : salas,
            }
    return render(request,'altera_salas.html', dados)






