from rest_framework import serializers
from ..models.produtoVenda import ProdutoVenda
from ..serializers.produto_serializer import ProdutoSerializer


class ProdutoVendaSerializer(serializers.ModelSerializer):
    produto = ProdutoSerializer()
    venda = serializers.SerializerMethodField()

    class Meta:
        model = ProdutoVenda
        fields = ['id', 'venda', 'produto']

    def get_venda(self, obj):
        return {
            'id': obj.venda.id,
            'data_venda': obj.venda.data_venda,
        } if obj.venda else None
