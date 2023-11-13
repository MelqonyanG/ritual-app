from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient


class EvaluateOperationViewTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = reverse('evaluate-operation')

    def test_evaluate_operation(self):
        data = {'expression': '2 + 2'}
        response = self.client.post(self.url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('result', response.data.keys())
        self.assertEqual(response.data['result'], 4)

    def test_evaluate_operation_with_invalid_data(self):
        data = {'expression': 'invalid_expression'}
        response = self.client.post(self.url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('error', response.data)
        self.assertEqual(response.data['error'], 'Invalid Expression.')
