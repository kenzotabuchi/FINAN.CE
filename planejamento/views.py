from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from perfil.models import Categoria, Conta
import json

def definir_planejamento(request):
    categorias = Categoria.objects.all()
    contexto = {
        'categorias': categorias,
    }
    return render(request, 'definir_planejamento.html', contexto)

@csrf_exempt
def update_valor_categoria(request, id):
    novo_valor = json.load(request)['novo_valor']
    categoria = Categoria.objects.get(id=id)
    categoria.valor_planejamento = novo_valor
    categoria.save()

    return JsonResponse({'status': 'Sucesso'})

def ver_planejamento(request):
    categorias = Categoria.objects.all()
    contexto = {
        'categorias': categorias,
    }
    return render(request, 'ver_planejamento.html', contexto)