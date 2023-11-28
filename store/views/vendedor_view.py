from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from ..models.vendedor import Vendedor
from ..serializers.vendedor_serializer import VendedorSerializer


@api_view(['GET', 'POST'])
def lista_vendedor(request, format=None):
    if request.method == 'GET':
        nome = request.query_params.get('nome', None)
        if nome:
            vendedores = Vendedor.objects.filter(nome__icontains=nome)
        else:
            vendedores = Vendedor.objects.all()

        serializer = VendedorSerializer(vendedores, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = VendedorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def lista_vendedor_id(request, id, format=None):
    try:
        vendedor = Vendedor.objects.get(pk=id)
    except Vendedor.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = VendedorSerializer(vendedor)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = VendedorSerializer(vendedor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        vendedor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
