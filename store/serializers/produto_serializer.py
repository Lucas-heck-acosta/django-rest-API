from rest_framework import serializers
from ..models.produto import Produto


class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = ['id', 'nome', 'descricao', 'preco',
                  'estoque', 'criado_em', 'atualizado_em']
