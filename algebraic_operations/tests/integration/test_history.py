from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

class OperationsHistoryViewTests(TestCase):
    def create_expressions(self, amount):
        data = {'expression': '2 + 2'}
        url = reverse('evaluate-operation')
        for _ in range(amount):
            response = self.client.post(url, data, format='json')

    def setUp(self):
        self.client = APIClient()
        self.url = reverse('operations-history')

    def test_operations_history_view(self):
        self.create_expressions(10)
        response = self.client.get(self.url, {'page_size': 10, 'page_number': 1})

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('history', response.data)
        self.assertEqual(len(response.data['history']), 10)

    def test_operations_history_view_invalid_params(self):
        response = self.client.get(self.url, {'page_size': 'invalid', 'page_number': -1})

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
