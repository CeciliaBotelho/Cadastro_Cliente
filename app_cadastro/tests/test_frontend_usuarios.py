from django.test import TestCase, Client

class FrontendTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_renderizacao_usuarios_html(self):
        response = self.client.get('/usuarios/')

        self.assertEqual(response.status_code, 200)

        self.assertTemplateUsed(response, 'usuarios/usuarios.html')
