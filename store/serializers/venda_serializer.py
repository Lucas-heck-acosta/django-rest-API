from rest_framework import serializers
from ..models.venda import Venda
from ..serializers.cliente_serializer import ClienteSerializer
from ..serializers.vendedor_serializer import VendedorSerializer
from ..serializers.produtoVenda_serializer import ProdutoVendaSerializer


class VendaSerializer(serializers.ModelSerializer):
    cliente = serializers.SerializerMethodField()
    vendedor = serializers.SerializerMethodField()

    class Meta:
        model = Venda
        fields = ['id', 'vendedor', 'cliente', 'data_venda', 'produtos']

    def get_cliente(self, obj):
        return obj.cliente.nome if obj.cliente else None

    def get_vendedor(self, obj):
        return obj.vendedor.nome if obj.vendedor else None

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['cliente'] = self.get_cliente(instance)
        representation['vendedor'] = self.get_vendedor(instance)
        return representation
