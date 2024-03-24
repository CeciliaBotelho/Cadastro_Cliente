from django.test import TestCase
from app_cadastro.fuzzy import calcular_credito

class FuzzyTestCase(TestCase):
    def test_calculate_credit(self):
        # Teste para verificar se a função calcular_credito retorna um valor válido
        # Teste com idade jovem e renda alta
        credito1 = calcular_credito(idade=25, renda_mensal=25000)
        self.assertTrue(credito1 >= 1500 and credito1 <= 60000)

        # Teste com idade média e renda média
        credito2 = calcular_credito(idade=50, renda_mensal=10000)
        self.assertTrue(credito2 >= 1500 and credito2 <= 60000)

        # Teste com idade idosa e renda baixa
        credito3 = calcular_credito(idade=70, renda_mensal=3000)
        self.assertTrue(credito3 >= 1500 and credito3 <= 60000)
