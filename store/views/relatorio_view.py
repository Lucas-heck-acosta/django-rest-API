from io import BytesIO
from datetime import datetime
from django.http import HttpResponse
from reportlab.pdfgen import canvas
from rest_framework.views import APIView
from ..models.venda import Venda
from ..serializers.venda_serializer import VendaSerializer
from ..models.produto import Produto


class RelatorioVendasPDF(APIView):
    def get(self, request):
        cliente = self.request.query_params.get('cliente', None)
        vendedor = self.request.query_params.get('vendedor', None)
        data_venda_min_str = self.request.query_params.get(
            'data_venda_min', None)
        data_venda_max_str = self.request.query_params.get(
            'data_venda_max', None)

        vendas = Venda.objects.all()
        if cliente:
            vendas = vendas.filter(cliente__nome__icontains=cliente)

        if vendedor:
            vendas = vendas.filter(vendedor__nome__icontains=vendedor)

        if data_venda_min_str:
            data_venda_min = datetime.strptime(data_venda_min_str, '%Y-%m-%d')
            vendas = vendas.filter(data_venda__gte=data_venda_min)

        if data_venda_max_str:
            data_venda_max = datetime.strptime(data_venda_max_str, '%Y-%m-%d')
            vendas = vendas.filter(data_venda__lte=data_venda_max)

        serializer = VendaSerializer(vendas, many=True)
        vendas_data = serializer.data

        pdf_buffer = BytesIO()
        p = canvas.Canvas(pdf_buffer)
        p.drawString(100, 800, "Relatório de Vendas")

        y = 780
        for venda in vendas_data:
            p.drawString(100, y, f"Data: {venda['data_venda']}")
            p.drawString(200, y, f"Cliente: {venda['cliente']}")
            p.drawString(400, y, f"Vendedor: {venda['vendedor']}")

            total_price = 0

            y -= 20
            for index, produto_id in enumerate(venda['produtos'], start=1):
                try:

                    produto = Produto.objects.get(pk=produto_id)

                    produto_info = f"Produto {index}: {
                        produto.nome}, Preço: {produto.preco}"

                    p.drawString(120, y, produto_info)
                    y -= 20

                    total_price += produto.preco
                except Produto.DoesNotExist:

                    pass

            p.drawString(120, y, f"Total Price: R${total_price}")

            y -= 30

        p.save()

        pdf_buffer.seek(0)

        response = HttpResponse(pdf_buffer, content_type='application/pdf')
        response['Content-Disposition'] = 'filename="relatorio_vendas.pdf"'
        return response
