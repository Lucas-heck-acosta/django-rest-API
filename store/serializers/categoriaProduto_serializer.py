from rest_framework import serializers
from ..models.categoriaProduto import CategoriaProduto


class CategoriaProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoriaProduto
        fields = ['id', 'nome']
