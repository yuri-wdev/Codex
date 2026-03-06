from django.shortcuts import render
from control.models import Livro

def dashboard(request):

    ## fazer funcao de contar os emprestimos ativos e inativos, e total de livros
    emprestimos_ativos = 15
    total_copias = 10
    total_livros = 120


    ## funcao de carregar os todos livros na tela

  


    livros = Livro.objects.all()
    total_livros = len(livros)
    total_copias= total_livros
    ## logica de carregar os livros na tela, e depois criar a função de contar os emprestimos ativos e inativos, e total de livros

    emprestimos = [
        {
            'cliente': 'João Silva',
            'livro': 'Dom Casmurro',
            'data_emprestimo': '01/03/2026',
            'data_devolucao': '15/03/2026',
            'status': 'Ativo'
        },
        {
            'cliente': 'Maria Oliveira',
            'livro': '1984',
            'data_emprestimo': '20/02/2026',
            'data_devolucao': '06/03/2026',
            'status': 'Pendente'
        },
        {
            'cliente': 'Carlos Souza',
            'livro': 'O Alquimista',
            'data_emprestimo': '10/02/2026',
            'data_devolucao': '24/02/2026',
            'status': 'Devolvido'
        },
        {
            'cliente': 'Ana Costa',
            'livro': 'O Senhor dos Anéis',
            'data_emprestimo': '02/03/2026',
            'data_devolucao': '16/03/2026',
            'status': 'Ativo'
        },
        {
            'cliente': 'Ricardo Lima',
            'livro': 'Harry Potter',
            'data_emprestimo': '15/01/2026',
            'data_devolucao': '29/01/2026',
            'status': 'Atrasado'
        },
    ]

    ## aqui vai cair a função de contar os emprestimos ativos e inativos, e total de livros
    context={
        'livros': livros,
        'emprestimos_ativos': emprestimos_ativos,
        'total_copias': total_copias,
        'total_livros': total_livros,
        'emprestimos': emprestimos
    }

    return render(request, "criando/criando.html", context)
