from django.shortcuts import render, redirect
from perfil.models import Conta, Categoria
from django.http import HttpResponse
from .models import Valores
from datetime import datetime
from xhtml2pdf import pisa
from django.template.loader import get_template

def novo_valor(request):
    if request.method == 'GET':
        status = request.GET.get('status')
        contas = Conta.objects.all()
        categorias = Categoria.objects.all()
        contexto = {
            'contas': contas,
            'categorias': categorias,
        }
        return render(request, 'novo_valor.html', contexto)
    
    elif request.method == 'POST':
        valor = request.POST.get('valor')
        categoria = request.POST.get('categoria')
        descricao = request.POST.get('descricao')
        data = request.POST.get('data')
        conta = request.POST.get('conta')
        tipo = request.POST.get('tipo')
        
        valores = Valores(
            valor=valor,
            categoria_id=categoria,
            descricao=descricao,
            data=data,
            conta_id=conta,
            tipo=tipo,
        )

        valores.save()
        conta = Conta.objects.get(id=conta)

        if tipo == 'E':
            conta.valor += int(valor)
        else:
            conta.valor -= int(valor)

        conta.save()

        return redirect('/extrato/novo_valor/?status=1')
    
def view_extrato(request):
    contas = Conta.objects.all()
    categorias = Categoria.objects.all() 
    valores = Valores.objects.filter(data__month=datetime.now().month)
    conta_get = request.GET.get('conta')
    categoria_get = request.GET.get('categoria')

    if conta_get:
        valores = valores.filter(conta__id=conta_get)
    if categoria_get:
        valores = valores.filter(categoria__id=categoria_get)

    contexto = {
        'valores': valores,
        'contas': contas,
        'categorias': categorias,
        }
    
    return render(request, 'view_extrato.html', contexto)

def exportar_pdf(request):
    valores = Valores.objects.filter(data__month=datetime.now().month)
    contas = Conta.objects.all()
    categorias = Categoria.objects.all()

    template = get_template('extrato_pdf.html')
    html = template.render({
        'valores': valores,
        'contas': contas,
        'categorias': categorias,
    })

    print(valores)

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename=extrato.pdf'

    # Gerar o PDF
    pisa_status = pisa.CreatePDF(html, dest=response)
    if pisa_status.err:
        return HttpResponse('Ocorreu um erro ao gerar o pdf')
    return response