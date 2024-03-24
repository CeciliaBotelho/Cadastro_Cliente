from django.test import TestCase, Client
from django.urls import reverse
from app_cadastro.models import Usuario

from django.test import TestCase, Client


class EditarUsuarioFrontendTest(TestCase):
    def setUp(self):
        # Criar um usuário de exemplo para testar a edição
        self.usuario = Usuario.objects.create(nome='Exemplo', idade=30, renda_mensal=3000)

        # Criar um cliente de teste
        self.client = Client()

    def test_renderizacao_editar_usuario_html(self):
        # Fazer uma solicitação GET para a página de edição do usuário
        response = self.client.get(reverse('editar_usuario', args=[self.usuario.id_usuario]))

        # Verificar se a resposta foi bem-sucedida (código 200)
        self.assertEqual(response.status_code, 200)

        # Verificar se o template correto foi usado
        self.assertTemplateUsed(response, 'usuarios/editar_usuario.html')
