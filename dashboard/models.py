# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Cliente(models.Model):
    idcliente = models.AutoField(db_column='idCliente', primary_key=True, blank=True, null=False)  
    nome = models.TextField(db_column='Nome', blank=True, null=False) 
    cpf = models.TextField(db_column='CPF', blank=True, null=False) 

    class Meta:
        managed = False
        db_table = 'Cliente'


class Emprestimo(models.Model):
    idemprestimo = models.AutoField(db_column='idEmprestimo', primary_key=True, blank=True, null=False) 
    idcliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='idCliente')  
    status = models.TextField(db_column='Status', blank=True, null=False)  
    codigo_livro = models.TextField(db_column='Codigo_livro', blank=True, null=False)  
    data_devolucao = models.TextField(blank=True, null=False)
    data_emprestimo = models.TextField(blank=True, null=False)
    quantidade = models.TextField(blank=True, null=False)

    class Meta:
        managed = False
        db_table = 'Emprestimo'


class Livros(models.Model):
    codigo = models.AutoField(db_column='Codigo', primary_key=True, blank=True, null=False)  
    titulo = models.TextField(db_column='Titulo') 
    autor = models.TextField(db_column='Autor')  
    quantidade = models.IntegerField(db_column='Quantidade')  
    genero = models.TextField(db_column='Genero') 

    class Meta:
        managed = False
        db_table = 'Livros'


class LivrosHasEmprestimo(models.Model):
    pk = models.CompositePrimaryKey('livros_codigo', 'emprestimo_idemprestimo')
    livros_codigo = models.ForeignKey(Livros, models.DO_NOTHING, db_column='Livros_Codigo')
    emprestimo_idemprestimo = models.ForeignKey(Emprestimo, models.DO_NOTHING, db_column='Emprestimo_idEmprestimo')

    class Meta:
        managed = False
        db_table = 'Livros_has_Emprestimo'
