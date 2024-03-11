from django.test import TestCase, Client
from rest_framework import status

import json
from decimal import Decimal

from .models import Extra

class ModeloTestCase(TestCase):
    fixtures = ['servicios_productos.json']

    def setUp(self):
        self.client = Client(HTTP_GET='localhost')

    def test_servicios_movilidad_toyota_ok(self):
        servicio_buscado = 'Toyota Mobility'
        response = self.client.get('/api/extra/toyota_mobility_service/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        content = json.loads(response.content)['results']
        self.assertLess(len(content), Extra.objects.all().count())

        for servicio in content:
            self.assertEqual(servicio['tipo'], 'Servicio')
            self.assertIn(servicio_buscado, servicio['nombre'])

