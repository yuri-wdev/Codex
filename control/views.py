from django.shortcuts import render, redirect
from .models import Livro
from django.contrib import messages


def control(request):
    nexid=Livro().get_next_id()

    livros = Livro.objects.all()

    livros_js = [
        {
            'id': livro.id,
            'titulo': livro.titulo,
            'autor': livro.autor,
            'ano': livro.ano_lancamento or 0, 
            'genero': livro.categoria or '',
            'quantidade': livro.quantidade_total or 0,
            'sinopse': livro.sinopse or ''
        }
        for livro in livros
    ]

    context = {
        'nexid': nexid,
        'livros': livros,
        'livros_js': livros_js
    }

    return render(request,"control/control.html", context)


def salvar_livro(request):
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        autor = request.POST.get('autor')
        categoria = request.POST.get('genero')
        publicacao = request.POST.get('ano')
        quantidade = request.POST.get('quantidade')
        sinopse = request.POST.get('sinopse')

        Livro().adicionar_livro(titulo, autor, categoria, publicacao, quantidade, sinopse)
        messages.success(request, f'📚 Livro "{titulo}" adicionado!')
        return redirect('controle')  # Redireciona após salvar

    return redirect('controle')  # Se não for POST, volta para control


def editar_livro(request):
    if request.method == 'POST':
        livro_id = request.POST.get('id_do_livro')
        titulo = request.POST.get('titulo')
        autor = request.POST.get('autor')
        categoria = request.POST.get('genero')
        publicacao = request.POST.get('ano')
        quantidade = request.POST.get('quantidade')
        sinopse = request.POST.get('sinopse')

        Livro().editar_livro(livro_id, titulo, autor, categoria, publicacao, quantidade, sinopse)
        messages.success(request, f'✏️ Livro "{titulo}" atualizado!')
        return redirect('controle')  # Redireciona após editar

    return redirect('controle')  # Se não for POST, volta para control

def remover_livro(request):
    if request.method == 'POST':
        id_livro = request.POST.get('id_do_livro')
        if id_livro:
            try:
                Livro().remover_livro(id_livro)
                messages.success(request, '🗑️ Livro removido com sucesso!')
            except Exception as e:
                messages.error(request, '❌ Erro ao remover livro.')
    return redirect('controle')