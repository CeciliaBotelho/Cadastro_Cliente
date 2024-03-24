from django.test import TestCase, Client

class FrontendTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_renderizacao_usuarios_html(self):
        # Faz uma solicitação GET para a página de usuários
        response = self.client.get('/usuarios/')

        # Verifica se a resposta foi bem-sucedida (código 200)
        self.assertEqual(response.status_code, 200)

        # Verifica se o template correto foi usado
        self.assertTemplateUsed(response, 'usuarios/usuarios.html')
