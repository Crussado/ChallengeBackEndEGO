from django.test import TestCase, Client
from rest_framework import status

import json
from decimal import Decimal

from .models import Modelo

class ModeloTestCase(TestCase):
    fixtures = ['modelos.json']

    def setUp(self):
        self.client = Client(HTTP_GET='localhost')

    def test_modelo_filter_carroceria_auto(self):
        """Es posible filtrar los modelos de los autos"""
        carrocerias_baneadas = ['Pickup', 'Comercial', 'Crossover', 'SUV']
        response = self.client.get('/api/modelo/?carroceria=auto')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        content = json.loads(response.content)

        self.assertLess(content['count'], Modelo.objects.all().count())
        for model in content['results']:
            Modelo.objects.get(pk=model['id']).carroceria.tipo
            self.assertNotIn(Modelo.objects.get(pk=model['id']).carroceria.tipo, carrocerias_baneadas)

    def test_modelo_filter_carroceria_SUV_Crossover(self):
        """Es posible filtrar los modelos de los SUV y Crossover"""
        carrocerias = ['Crossover', 'SUV']
        response = self.client.get('/api/modelo/?carroceria=syc')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        content = json.loads(response.content)

        self.assertLess(content['count'], Modelo.objects.all().count())
        for model in content['results']:
            Modelo.objects.get(pk=model['id']).carroceria.tipo
            self.assertIn(Modelo.objects.get(pk=model['id']).carroceria.tipo, carrocerias)

    def test_modelo_gazoo_racing(self):
        response = self.client.get('/api/modelo/toyota_gazoo_racing/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        content = json.loads(response.content)
        self.assertEqual(content['nombre'], 'Gazoo Racing')
        self.assertEqual(content['marca'], 'Toyota')

    def test_modelo_toyota_hibridos(self):
        partes = ['Transmision automatica', 'Transmision manual']

        response = self.client.get('/api/modelo/toyota_hibridos/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        content = json.loads(response.content)['results']
        self.assertLess(len(content), Modelo.objects.all().count())

        for model in content:
            partes_model = [parte['nombre'] for parte in model['partes']]
            self.assertIn(partes[0], partes_model)
            self.assertIn(partes[1], partes_model)

    def test_modelo_innovacion(self):
        response = self.client.get('/api/modelo/innovacion/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        content = json.loads(response.content)['results']
        self.assertLess(len(content), Modelo.objects.all().count())

        last_year = Decimal(content[0]['anio'])
        for model in content:
            actual_model_year = Decimal((model['anio']))
            self.assertGreaterEqual(last_year, actual_model_year)
            last_year = actual_model_year

    def test_modelo_precio_orden(self):
        def check_precio_odern(content):
            lower_price = Decimal(content[0]['precio'])
            for model in content:
                actual_model_price = Decimal((model['precio']))
                self.assertLessEqual(lower_price, actual_model_price)
                lower_price = actual_model_price

        response = self.client.get('/api/modelo/?ordering=precio')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        content = json.loads(response.content)['results']
        self.assertEqual(len(content), Modelo.objects.all().count())

        check_precio_odern(content)

        response = self.client.get('/api/modelo/?ordering=precio&carroceria=syc')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        content = json.loads(response.content)['results']
        self.assertLess(len(content), Modelo.objects.all().count())

        check_precio_odern(content)
