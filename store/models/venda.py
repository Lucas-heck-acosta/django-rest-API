from django.db import models
from ..models.vendedor import Vendedor
from ..models.cliente import Cliente
from ..models.produto import Produto


class Venda(models.Model):
    vendedor = models.ForeignKey(Vendedor, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    data_venda = models.DateField()
    produtos = models.ManyToManyField(Produto, through='ProdutoVenda')

    def __str__(self):
        return f'{self.data_venda} - {self.cliente} - {self.vendedor}'
