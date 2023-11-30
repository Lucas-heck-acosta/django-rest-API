from django.db import models
from ..models.venda import Venda
from ..models.produto import Produto


class ProdutoVenda(models.Model):
    venda = models.ForeignKey(Venda, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.produto} em venda: {self.venda}'
