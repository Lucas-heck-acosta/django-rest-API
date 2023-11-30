from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from ..models.produtoVenda import ProdutoVenda
from ..serializers.produtoVenda_serializer import ProdutoVendaSerializer


@api_view(['GET', 'POST'])
def lista_produto_vendas(request, format=None):
    if request.method == 'GET':
        produtos = ProdutoVenda.objects.all()
        serializer = ProdutoVendaSerializer(produtos, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ProdutoVendaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def lista_produto_vendas_id(request, id, format=None):
    try:
        produto = ProdutoVenda.objects.get(pk=id)
    except ProdutoVenda.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ProdutoVendaSerializer(produto)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ProdutoVendaSerializer(produto, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        produto.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
