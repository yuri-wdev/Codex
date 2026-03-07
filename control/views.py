from django.shortcuts import render, redirect
from dashboard.models import Livros, Emprestimo, Cliente
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required
def control(request):
    livros = Livros.objects.all()

    livros_js = [
        {
            'id': livro.codigo,
            'titulo': livro.titulo,
            'autor': livro.autor,
            'genero': livro.genero or '',
            'quantidade': livro.quantidade or 0,
        }
        for livro in livros
    ]

    context = {
        'livros': livros,
        'livros_js': livros_js
    }

    return render(request, "control/control.html", context)


@login_required
def salvar_livro(request):
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        autor = request.POST.get('autor')
        genero = request.POST.get('genero')
        quantidade = request.POST.get('quantidade')

        Livros.objects.create(
            titulo=titulo,
            autor=autor,
            genero=genero,
            quantidade=quantidade,
        )
        messages.success(request, f'📚 Livro "{titulo}" adicionado!')
        return redirect('controle')

    return redirect('controle')


@login_required
def editar_livro(request):
    if request.method == 'POST':
        livro_id = request.POST.get('id_do_livro')
        titulo = request.POST.get('titulo')
        autor = request.POST.get('autor')
        genero = request.POST.get('genero')
        quantidade = request.POST.get('quantidade')

        try:
            livro = Livros.objects.get(codigo=livro_id)
            if titulo:    livro.titulo    = titulo
            if autor:     livro.autor     = autor
            if genero:    livro.genero    = genero
            if quantidade: livro.quantidade = quantidade
            livro.save()
            messages.success(request, f'✏️ Livro "{livro.titulo}" atualizado!')
        except Livros.DoesNotExist:
            messages.error(request, '❌ Livro não encontrado.')

    return redirect('controle')


@login_required
def remover_livro(request):
    if request.method == 'POST':
        id_livro = request.POST.get('id_do_livro')
        try:
            livro = Livros.objects.get(codigo=id_livro)
            livro.delete()
            messages.success(request, '🗑️ Livro removido com sucesso!')
        except Livros.DoesNotExist:
            messages.error(request, '❌ Livro não encontrado.')

    return redirect('controle')


@login_required
def salvar_emprestimo(request):
    if request.method == 'POST':
        codigo_livro = request.POST.get('codigo_livro')
        idcliente = request.POST.get('idcliente')
        data_emprestimo = request.POST.get('data_emprestimo')
        data_devolucao = request.POST.get('data_devolucao')

        try:
            cliente = Cliente.objects.get(idcliente=idcliente)
            Emprestimo.objects.create(
                codigo_livro=codigo_livro,
                idcliente=cliente,
                data_emprestimo=data_emprestimo,
                data_devolucao=data_devolucao,
                status='Ativo'
            )
            messages.success(request, '📖 Empréstimo registrado com sucesso!')
        except Cliente.DoesNotExist:
            messages.error(request, '❌ Cliente não encontrado.')
        except Exception as e:
            messages.error(request, f'❌ Erro: {e}')

    return redirect('controle')


@login_required
def devolver_emprestimo(request):
    if request.method == 'POST':
        idemprestimo = request.POST.get('idemprestimo')

        try:
            emp = Emprestimo.objects.get(idemprestimo=idemprestimo)
            emp.status = 'Devolvido'
            emp.save()
            messages.success(request, '✅ Devolução registrada com sucesso!')
        except Emprestimo.DoesNotExist:
            messages.error(request, '❌ Empréstimo não encontrado.')

    return redirect('controle')

@login_required
def salvar_cliente(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        cpf = request.POST.get('cpf')

        Cliente.objects.create(nome=nome, cpf=cpf)
        messages.success(request, f'👤 Cliente "{nome}" cadastrado!')

    return redirect('controle')