from fin.models import Despesa, Categoria, Salario
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login, logout
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.paginator import Paginator
from datetime import date


def transforma_mes(num):
    meses = {1:"Janeiro",2:"Fevereiro",3:"Março",4:"Abril",5:"Maio",6:"Junho",7:"Julho",8:"Agosto",9:"Setembro",
             10:"Outubro",11:"Novembro",12:"Dezembro"}
    mes = meses[num]
    return mes

def login_user(reuest):
    return render(reuest,'login.html')

def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('pass')
        usuario = authenticate(username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect('/')
        else:
            messages.error(request, "Usuário ou senha inválido")
    return redirect('/login')

def logout_sistema(request):
    logout(request)
    return redirect('/')

@login_required(login_url='/login/')
def grafico_financeiro(request):
    return render(request, 'financeiro.html')

@login_required(login_url='/login/')
def visual_salario(request):
    data_at = date.today()
    mes_atual = data_at.month
    mes_ant = (mes_atual - 1)
    nome_mes_atual = transforma_mes(mes_atual)
    nome_mes_anterior = transforma_mes(mes_ant)
    slt_at = 0
    slt_ant = 0
    salario_atual = Salario.objects.values('valor_sal').filter(data_sal__month=mes_atual)
    salario_ant = Salario.objects.values('valor_sal').filter(data_sal__month=mes_ant)
    if salario_atual:
        slt_at = salario_atual[0]['valor_sal']
    if salario_ant:
        slt_ant = salario_ant[0]['valor_sal']

    # print(salario_atual)
    # print(type(slt_at))
    # print(slt_at)
    # print(slt_at.query)
    dados = {'mes_atual':nome_mes_atual, 'mes_anterior':nome_mes_anterior, 'sl_atual':slt_at, 'sl_anterior':slt_ant}
    return render(request, 'salario.html', dados)

@login_required(login_url='/login/')
def cadastrar_salario(request):
    return render(request, 'cadastro_salario.html')

@login_required(login_url='/login/')
def visual_despesas(request):
    return render(request,'despesas.html')

@login_required(login_url='/login/')
def cadastrar_despesa(request):
    lcat = Categoria.objects.all()
    dados = {'ls_cat': lcat}
    return render(request,'cadastro_despesa.html', dados)

@login_required(login_url='/login/')
def submit_despesa(request):
    if request.POST:
        valor = request.POST.get('valor')
        nome = request.POST.get('nome')
        data = request.POST.get('data')
        categoria = request.POST.get('categoria')
        id_categoria = Categoria.objects.get(id=categoria)

        Despesa.objects.create(valor_dep=valor,
                               nome_desp=nome,
                               data_dep=data,
                               cat_dep=id_categoria)
    return redirect('/despesas')

@login_required(login_url='/login/')
def visual_categoria(request):
    lcat = Categoria.objects.all()
    dados = {'ls_cat':lcat}
    return render(request,'categoria.html', dados)

@login_required(login_url='/login/')
def cadastrar_categoria(request):
    return render(request,'cadastro_categoria.html')

@login_required(login_url='/login/')
def submit_categoria(request):
    if request.POST:
        categoria = request.POST.get('cat')
        Categoria.objects.create(nome_cat=categoria)
    return redirect('/despesas/categoria')
