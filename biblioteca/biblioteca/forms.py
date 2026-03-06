#criando um formulário para atualizar os dados do livro
from django import forms
from ProjetoFinal_Cepedi.biblioteca.gestao.models import Cliente, Livro, Emprestimo, ItemEmprestimo, Movimentacao

class LivroForm(forms.ModelForm):
    class Meta:
        model = Livro
        fields = ['titulo', 'autores', 'quantidade_total', 'categoria', 'ano_lancamento']

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'cpf']

class EmprestimoForm(forms.ModelForm):
    class Meta:
        model = Emprestimo
        fields = ['livro', 'cliente', 'data_prevista_devolucao']

class ItemEmprestimoForm(forms.ModelForm):
    class Meta:
        model = ItemEmprestimo
        fields = ['emprestimo', 'livro', 'quantidade']

class MovimentacaoForm(forms.ModelForm):
    class Meta:
        model = Movimentacao
        fields = ['livro', 'tipo', 'quantidade', 'usuario'] 