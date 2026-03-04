#criando um formulário para atualizar os dados do livro usando ModelForm do Django
from django import forms
from .models import Livro
#criando a classe LivroForm que herda de forms.ModelForm para criar um formulário baseado no modelo Livro
class LivroForm(forms.ModelForm):
    class Meta:
        model = Livro
        fields = ['titulo', 'autor', 'quantidade']  # coloque aqui os campos que quer atualizar
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'autor': forms.TextInput(attrs={'class': 'form-control'}),
            'quantidade': forms.NumberInput(attrs={'class': 'form-control'}),
        }