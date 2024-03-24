from django.test import TestCase, Client
from django.urls import reverse
from app_cadastro.models import Usuario

from django.test import TestCase, Client


class EditarUsuarioFrontendTest(TestCase):
    def setUp(self):
        self.usuario = Usuario.objects.create(nome='Exemplo', idade=30, renda_mensal=3000)

        self.client = Client()

    def test_renderizacao_editar_usuario_html(self):
        response = self.client.get(reverse('editar_usuario', args=[self.usuario.id_usuario]))

        self.assertEqual(response.status_code, 200)

        self.assertTemplateUsed(response, 'usuarios/editar_usuario.html')
