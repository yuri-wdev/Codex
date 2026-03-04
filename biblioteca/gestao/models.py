from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# -----------------------
# Model Livro
# -----------------------
class Livro(models.Model):
    titulo = models.CharField(max_length=255)
    sinopse = models.TextField()
    autores = models.CharField(max_length=255)
    categoria = models.CharField(max_length=100)
    ano_lancamento = models.IntegerField()
    quantidade_total = models.IntegerField()
    quantidade_disponivel = models.IntegerField()
    interager = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='livros')

    def __str__(self):
        return self.titulo

    # Métodos úteis
    def emprestar(self, quantidade=1):
        if self.quantidade_disponivel >= quantidade:
            self.quantidade_disponivel -= quantidade
            self.save()
            return True
        return False

    def devolver(self, quantidade=1):
        self.quantidade_disponivel += quantidade
        if self.quantidade_disponivel > self.quantidade_total:
            self.quantidade_disponivel = self.quantidade_total
        self.save()

    @classmethod
    def listar_disponiveis(cls):
        return cls.objects.filter(quantidade_disponivel__gt=0)


# -----------------------
# Model Cliente
# -----------------------
class Cliente(models.Model):
    nome = models.CharField(max_length=255)
    cpf = models.CharField(max_length=14, unique=True)

    def __str__(self):
        return f"{self.nome} ({self.cpf})"

    @classmethod
    def buscar_por_cpf(cls, cpf):
        return cls.objects.get(cpf=cpf)


# -----------------------
# Model Emprestimo
# -----------------------
class Emprestimo(models.Model):
    STATUS_CHOICES = [
        ('EM_ANDAMENTO', 'Em andamento'),
        ('ATRASADO', 'Atrasado'),
        ('DEVOLVIDO', 'Devolvido'),
    ]

    livro = models.ForeignKey(Livro, on_delete=models.CASCADE, related_name='emprestimos')
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='emprestimos')
    data_emprestimo = models.DateField(default=timezone.now)
    data_prevista_devolucao = models.DateField()
    data_devolucao = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='EM_ANDAMENTO')

    def __str__(self):
        return f"{self.livro.titulo} -> {self.cliente.nome} ({self.status})"

    # Métodos úteis
    def marcar_devolvido(self):
        if self.status != 'DEVOLVIDO':
            self.status = 'DEVOLVIDO'
            self.data_devolucao = timezone.now().date()
            self.livro.devolver()  # devolve automaticamente no estoque
            self.save()

    def verificar_atraso(self):
        if self.status == 'EM_ANDAMENTO' and timezone.now().date() > self.data_prevista_devolucao:
            self.status = 'ATRASADO'
            self.save()


# -----------------------
# Model ItemEmprestimo
# -----------------------
class ItemEmprestimo(models.Model):
    emprestimo = models.ForeignKey(Emprestimo, on_delete=models.CASCADE, related_name='itens')
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.livro.titulo} - {self.quantidade}"

    # Ao salvar o item, reduz a quantidade disponível do livro
    def save(self, *args, **kwargs):
        if not self.pk:  # só na criação
            if not self.livro.emprestar(self.quantidade):
                raise ValueError(f"Não há {self.quantidade} exemplares disponíveis de {self.livro.titulo}")
        super().save(*args, **kwargs)


# -----------------------
# Model Movimentacao
# -----------------------
class Movimentacao(models.Model):
    TIPO_CHOICES = [
        ('E', 'Entrada'),
        ('S', 'Saida'),
    ]

    livro = models.ForeignKey(Livro, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=1, choices=TIPO_CHOICES)
    quantidade = models.PositiveIntegerField()
    data = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.livro.titulo} - {self.get_tipo_display()}"

    def save(self, *args, **kwargs):
        if not self.pk:  # só na criação
            if self.tipo == 'E':
                self.livro.quantidade_disponivel += self.quantidade
                self.livro.quantidade_total += self.quantidade
            else:
                if self.livro.quantidade_disponivel < self.quantidade:
                    raise ValueError("Não há livros suficientes para saída")
                self.livro.quantidade_disponivel -= self.quantidade
            self.livro.save()
        super().save(*args, **kwargs)