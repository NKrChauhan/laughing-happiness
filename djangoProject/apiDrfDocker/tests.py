from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
import json


class ApiDRFDockerTest(APITestCase):
    def test_hello_world(self):
        url = reverse('apiDrfDocker:hello_world')
        response = self.client.get(url)
        response_data = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response_data['response'], 'Hello world')
