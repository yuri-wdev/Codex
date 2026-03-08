from symtable import Class

from django.db import models

# Create your models here.

class Livro(models.Model):

    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=100)
    sinopse = models.TextField()
    categoria = models.CharField(max_length=50) 
    ano_lancamento = models.CharField(max_length=4)
    quantidade_total = models.IntegerField()
    


    def __str__(self):
        return self.titulo

    def adicionar_livro(self, titulo, autor, categoria, publicacao, quantidade, sinopse):
        livro = Livro(
            titulo=titulo,
            autor=autor,
            sinopse=sinopse,
            categoria=categoria,
            ano_lancamento=publicacao,
            quantidade_total=quantidade
            
        )
        livro.save()
    
    def editar_livro(self, id, titulo, autor, categoria, publicacao, quantidade, sinopse):
        print(f"Editando livro com id: {id}")
        try:
            livro = Livro.objects.get(id=id)

            livro.titulo = titulo
            livro.autor = autor
            livro.categoria = categoria
            livro.ano_lancamento = publicacao
            livro.quantidade_total = quantidade
            livro.sinopse = sinopse
            livro.save()
        except Livro.DoesNotExist:
            print(f"Livro com id {id} não encontrado.")
    

    def remover_livro(self, id):
        try:
            livro = Livro.objects.get(id=id)
            livro.delete()
        except Livro.DoesNotExist:
            print(f"Livro com id {id} não encontrado.")

    def get_next_id(self):
        last_livro = Livro.objects.order_by('id').last()
        if last_livro:
            return last_livro.id + 1
        else:
            return 1