from datetime import datetime
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from ..models.venda import Venda
from ..serializers.venda_serializer import VendaSerializer


@api_view(['GET', 'POST'])
def lista_vendas(request, format=None):
    if request.method == 'GET':
        cliente = request.query_params.get('cliente', None)
        vendedor = request.query_params.get('vendedor', None)
        data_venda_str = request.query_params.get('data_venda', None)
        data_venda_min_str = request.query_params.get('data_venda_min', None)
        data_venda_max_str = request.query_params.get('data_venda_max', None)

        vendas = Venda.objects.all()
        if cliente:
            vendas = vendas.filter(cliente__nome__icontains=cliente)

        if vendedor:
            vendas = vendas.filter(vendedor__nome__icontains=vendedor)

        if data_venda_str:
            data_venda = datetime.strptime(data_venda_str, '%Y-%m-%d')
            vendas = vendas.filter(data_venda=data_venda)

        if data_venda_min_str:
            data_venda_min = datetime.strptime(data_venda_min_str, '%Y-%m-%d')
            vendas = vendas.filter(data_venda__gte=data_venda_min)

        if data_venda_max_str:
            data_venda_max = datetime.strptime(data_venda_max_str, '%Y-%m-%d')
            vendas = vendas.filter(data_venda__lte=data_venda_max)

        serializer = VendaSerializer(vendas, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = VendaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def lista_vendas_id(request, id, format=None):
    try:
        venda = Venda.objects.get(pk=id)
    except Venda.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = VendaSerializer(venda)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = VendaSerializer(venda, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        venda.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
