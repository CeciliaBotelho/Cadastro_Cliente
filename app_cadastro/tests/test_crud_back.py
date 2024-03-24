from django.test import TestCase
from app_cadastro.models import Usuario 

class CRUDTestCase(TestCase):
    def setUp(self):
        Usuario.objects.create(nome='João', idade=30, renda_mensal=2000)

    def test_create(self):
        Usuario.objects.create(nome='Maria', idade=25, renda_mensal=3000)
        self.assertEqual(Usuario.objects.count(), 2)

    def test_read(self):
        usuario = Usuario.objects.get(nome='João')
        self.assertEqual(usuario.idade, 30)

    def test_update(self):
        usuario = Usuario.objects.get(nome='João')
        usuario.idade = 35
        usuario.save()
        self.assertEqual(Usuario.objects.get(nome='João').idade, 35)

    def test_delete(self):
        usuario = Usuario.objects.get(nome='João')
        usuario.delete()
        self.assertEqual(Usuario.objects.count(), 0)
