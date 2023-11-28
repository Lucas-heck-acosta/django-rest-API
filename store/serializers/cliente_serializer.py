from rest_framework import serializers
from ..models.cliente import Cliente


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['id', 'nome', 'email', 'telefone',
                  'endereco', 'data_nascimento']
