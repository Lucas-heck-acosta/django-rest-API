from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from ..models.categoriaProduto import CategoriaProduto
from ..serializers.categoriaProduto_serializer import CategoriaProdutoSerializer


@api_view(['GET', 'POST'])
def lista_categorias(request, format=None):
    if request.method == 'GET':
        nome = request.query_params.get('nome', None)

        if nome:
            categoria = CategoriaProduto.objects.filter(nome__icontains=nome)
        else:
            categoria = CategoriaProduto.objects.all()

        serializer = CategoriaProdutoSerializer(categoria, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = CategoriaProdutoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def lista_categorias_id(request, id, format=None):
    try:
        categoria = CategoriaProduto.objects.get(pk=id)
    except CategoriaProduto.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CategoriaProdutoSerializer(categoria)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = CategoriaProdutoSerializer(categoria, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        categoria.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
