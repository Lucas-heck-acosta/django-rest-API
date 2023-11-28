from rest_framework import serializers
from ..models.vendedor import Vendedor


class VendedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendedor
        fields = ['id', 'nome', 'email', 'telefone']
