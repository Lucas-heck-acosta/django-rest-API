from django.test import TestCase
from datetime import date
from store.models.cliente import Cliente


class ClienteModelTestCase(TestCase):
    def setUp(self):
        Cliente.objects.create(
            nome="Teste Cliente",
            email="teste@cliente.com",
            telefone="123456789",
            endereco="Rua Teste, 123",
            data_nascimento=date(1990, 1, 1)
        )

    def test_cliente_str(self):
        cliente = Cliente.objects.get(nome="Teste Cliente")
        self.assertEqual(str(cliente), "Teste Cliente - teste@cliente.com")

    def test_cliente_data_nascimento_nula(self):
        cliente = Cliente.objects.create(
            nome="Cliente Sem Data",
            email="semdata@cliente.com",
            telefone="987654321"
        )
        self.assertIsNone(cliente.data_nascimento)
