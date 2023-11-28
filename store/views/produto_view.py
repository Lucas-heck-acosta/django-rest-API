from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from ..models.produto import Produto
from ..serializers.produto_serializer import ProdutoSerializer


@api_view(['GET', 'POST'])
def lista_produto(request, format=None):
    if request.method == 'GET':
        nome = request.query_params.get('nome', None)
        preco_minimo = request.query_params.get('preco_minimo', None)
        preco_maximo = request.query_params.get('preco_maximo', None)

        produtos = Produto.objects.all()

        if nome:
            produtos = produtos.filter(nome__icontains=nome)

        if preco_minimo:
            produtos = produtos.filter(preco__gte=preco_minimo)

        if preco_maximo:
            produtos = produtos.filter(preco__lte=preco_maximo)

        serializer = ProdutoSerializer(produtos, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ProdutoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def lista_produto_id(request, id, format=None):
    try:
        produto = Produto.objects.get(pk=id)
    except Produto.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ProdutoSerializer(produto)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ProdutoSerializer(produto, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        produto.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
