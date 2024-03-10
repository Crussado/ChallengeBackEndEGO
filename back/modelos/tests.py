from django.test import TestCase, Client
from rest_framework import status

import json

from .models import Modelo

class ModeloTestCase(TestCase):
    fixtures = ['modelos.json']

    def setUp(self):
        self.client = Client(HTTP_GET='localhost')

    def test_modelo_filter_carroceria(self):
        """Es posible filtrar los modelos de los autos"""
        carrocerias_baneadas = ['Pickup', 'Comercial', 'Pickup', 'SUV']
        response = self.client.get('/api/modelo/?carroceria=auto')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        content = json.loads(response.content)

        self.assertLess(content['count'], Modelo.objects.all().count())
        for model in content['results']:
            Modelo.objects.get(pk=model['id']).carroceria.tipo
            self.assertNotIn(Modelo.objects.get(pk=model['id']).carroceria.tipo, carrocerias_baneadas)
