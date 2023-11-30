from rest_framework import serializers
from ..models.venda import Venda


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
