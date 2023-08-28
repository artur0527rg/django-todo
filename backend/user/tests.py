from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase



class AccountTests(APITestCase):
    def setUp(self) -> None:
        self.url = reverse('signup')

    def test_invalid_user_data(self):
        response = self.client.post(self.url)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_valid_user_data(self):
        data = {
            'username': 'test',
            'password': 'test1234test',
            'email': 'test@gmail.com'
        }
        response = self.client.post(self.url, data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        response = response.json()
        self.assertEqual(response['username'], data['username'])
        self.assertEqual(response['email'], data['email'])
