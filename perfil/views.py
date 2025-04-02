from django.shortcuts import render, redirect
from .models import Categoria, Conta
from extrato.models import Valores
from django.contrib import messages
from django.contrib.messages import constants
from django.db.models import Sum
from .utils import calcula_total, calcula_equilibrio_financeiro
from datetime import datetime

def home(request):
    valores = Valores.objects.filter(data__month=datetime.now().month)
    entradas = valores.filter(tipo='E')
    saidas = valores.filter(tipo='S')

    total_entradas = calcula_total(entradas, 'valor')
    total_saidas = calcula_total(saidas, 'valor')

    contas = Conta.objects.all()
    total_contas = calcula_total(contas, 'valor')

    percentual_gastos_essenciais, percentual_gastos_nao_essenciais = calcula_equilibrio_financeiro()

    contexto = {
        'contas': contas,
        'total_contas': total_contas,
        'total_entradas': total_entradas,
        'total_saidas': total_saidas,
        'percentual_gastos_essenciais': int(percentual_gastos_essenciais),
        'percentual_gastos_nao_essenciais': int(percentual_gastos_nao_essenciais),
        
    }
    return render(request, 'home.html', contexto)

def gerenciar(request):
    status = request.GET.get('status')
    contas = Conta.objects.all()
    categorias = Categoria.objects.all()
    # total_contas = contas.aggregate(Sum('valor'))
    total_contas = calcula_total(contas, 'valor')
    contexto = {
        'contas': contas,
        'status': status,
        'total_contas': total_contas,
        'categorias': categorias,
    }
    return render(request, 'gerenciar.html', contexto)

def cadastrar_banco(request):
    apelido = request.POST.get('apelido')
    banco = request.POST.get('banco')
    tipo = request.POST.get('tipo')
    valor = request.POST.get('valor')
    icone = request.FILES.get('icone')
    
    if len(apelido.strip()) == 0 or len(valor.strip()) == 0:
        return redirect('/perfil/gerenciar/?status=2')
    
    # TO-DO: fazer mais validações

    conta = Conta(
        apelido = apelido,
        banco=banco,
        tipo=tipo,
        valor=valor,
        icone=icone
    )

    conta.save()

    return redirect('/perfil/gerenciar/?status=1')

def deletar_banco(request, id):
    conta = Conta.objects.get(id=id)
    conta.delete()

    return redirect('/perfil/gerenciar/?status=3')

def cadastrar_categoria(request):
    nome = request.POST.get('categoria')
    essencial = bool(request.POST.get('essencial'))

    # TO-DO: fazer validações

    categoria = Categoria(
        categoria=nome,
        essencial=essencial
    )

    categoria.save()

    return redirect('/perfil/gerenciar/?status=4')

def update_categoria(request, id):
    categoria = Categoria.objects.get(id=id)
    categoria.essencial = not categoria.essencial
    categoria.save()

    return redirect('/perfil/gerenciar/')

def dashboard(request):
    dados = {}
    categorias = Categoria.objects.all()

    for categoria in categorias:
        dados[categoria.categoria] = Valores.objects.filter(categoria=categoria).filter(tipo='S').filter(data__month=datetime.now().month).aggregate(Sum('valor'))['valor__sum'] or 0


    contexto = {
        'dados': dados,
        'categorias': categorias,
        'labels': list(dados.keys()),
        'values': list(dados.values()),
    }

    return render(request, 'dashboard.html', contexto)