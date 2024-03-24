from django.test import TestCase, Client
from django.urls import reverse

class FrontendTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_renderizacao_home_html(self):
        response = self.client.get(reverse('home'))

        self.assertEqual(response.status_code, 200)

        self.assertTemplateUsed(response, 'usuarios/home.html')
