from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from dashboard.models import Livros, Emprestimo

@login_required
def dashboard(request):
    livros = Livros.objects.all()
    emprestimos = Emprestimo.objects.all()

    total_livros = livros.count()
    total_copias = sum(l.quantidade for l in livros)
    emprestimos_ativos = emprestimos.filter(status='Ativo').count()

    context = {
        'livros': livros,
        'emprestimos': emprestimos,
        'total_livros': total_livros,
        'total_copias': total_copias,
        'emprestimos_ativos': emprestimos_ativos,
    }

    return render(request, "criando/criando.html", context)