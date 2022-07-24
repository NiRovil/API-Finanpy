from django.test import TestCase
from financeiro.models import Receitas

class TestesTestCase(TestCase):

    def setUp(self):
        self.receita = Receitas.objects.create(
            descricao = 'Venda de ativo',
            valor = 100,
        )

    def test_atributos(self):
        self.assertEqual(self.receita.descricao, 'Venda de ativo')
        self.assertEqual(self.receita.valor, 100)