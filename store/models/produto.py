from xml.dom import ValidationErr
from django.db import models
from store.models.categoriaProduto import CategoriaProduto


class Produto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    estoque = models.PositiveIntegerField(default=0)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    categoria = models.ForeignKey(
        CategoriaProduto, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome + ' - R$' + str(self.preco)
