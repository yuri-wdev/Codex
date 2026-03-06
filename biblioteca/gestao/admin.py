from django.contrib import admin
from .models import Livro, Emprestimo, ItemEmprestimo, Movimentacao, Cliente

# -----------------------
# Admin Livro
# -----------------------
@admin.register(Livro)
class LivroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autores', 'quantidade_total', 'quantidade_disponivel', 'categoria', 'ano_lancamento')
    search_fields = ('titulo', 'autores', 'categoria')

# -----------------------
# Admin Movimentacao
# -----------------------
@admin.register(Movimentacao)
class MovimentacaoAdmin(admin.ModelAdmin):
    list_display = ('livro', 'tipo', 'quantidade', 'data', 'usuario')
    list_filter = ('tipo', 'data', 'usuario')
    search_fields = ('livro__titulo', 'usuario__username')

# -----------------------
# Admin Emprestimo
# -----------------------
@admin.register(Emprestimo)
class EmprestimoAdmin(admin.ModelAdmin):
    list_display = ('id', 'livro', 'cliente', 'data_emprestimo', 'data_prevista_devolucao', 'status')
    list_filter = ('status', 'data_emprestimo', 'data_prevista_devolucao')
    search_fields = ('livro__titulo', 'cliente__nome')

# -----------------------
# Admin ItemEmprestimo
# -----------------------
@admin.register(ItemEmprestimo)
class ItemEmprestimoAdmin(admin.ModelAdmin):
    list_display = ('emprestimo', 'livro', 'quantidade')
    list_filter = ('emprestimo', 'livro')
    search_fields = ('livro__titulo', 'emprestimo__id')

# -----------------------
# Admin Cliente (opcional, mas útil)
# -----------------------
@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cpf')
    search_fields = ('nome', 'cpf')