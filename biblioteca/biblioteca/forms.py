#criando um formulário para atualizar os dados do livro
from django import forms
from .models import Livro

class LivroForm(forms.ModelForm):
    class Meta:
        model = Livro
        fields = ['titulo', 'autores', 'quantidade_total', 'categoria', 'ano_lancamento']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'autores': forms.TextInput(attrs={'class': 'form-control'}),
            'quantidade_total': forms.NumberInput(attrs={'class': 'form-control'}), 
            'categoria': forms.TextInput(attrs={'class': 'form-control'}),
            'ano_lancamento': forms.NumberInput(attrs={'class': 'form-control'}),
        }           