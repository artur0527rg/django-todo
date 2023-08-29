from django.urls import reverse
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from rest_framework import status
from rest_framework.test import APITestCase

User = get_user_model()

class AccountTests(APITestCase):
    def setUp(self) -> None:
        self.url = reverse('user-view')
        self.HEADER_TYPES = 'Bearer '

        self.data = {
            'username': 'user',
            'password': 'user',
            'email' : 'user@gmail.com',
        }
        User.objects.create(
            **{
                **self.data,
                'password': make_password(self.data['password'])
            }
        )
        self.token = self.client.post(reverse('token_obtain_pair'), data=self.data).json()

    def test_invalid_user_data(self):
        response = self.client.post(self.url)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_valid_user_data(self):
        self.data = {
            'username': 'test',
            'password': 'test1234test',
            'email': 'test@gmail.com'
        }
        response = self.client.post(self.url, data=self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        response = response.json()
        self.assertEqual(response['username'], self.data['username'])
        self.assertEqual(response['email'], self.data['email'])

    def test_get_profile(self):
        response = self.client.get(
            self.url,
            headers = {
                'Authorization': self.HEADER_TYPES + self.token['access'],
            },
        )
        response = response.json()
        self.assertEqual(response['username'], self.data['username'])
        self.assertEqual(response['email'], self.data['email'])

    def test_patch_profile(self):
        new_email = 'test_new@gmail.com'
        response = self.client.patch(
            self.url,
            headers = {
                'Authorization': self.HEADER_TYPES + self.token['access'],
            },
            data = {
                'email': new_email,
            }
        )
        response = response.json()
        self.assertEqual(response['username'], self.data['username'])
        self.assertEqual(response['email'], new_email)

    def test_delete_profile(self):
        response = self.client.delete(
            self.url,
            headers = {
                'Authorization': self.HEADER_TYPES + self.token['access']
            },    
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        
        response = self.client.get(
            self.url,
            headers = {
                'Authorization': self.HEADER_TYPES + self.token['access'],
            },
        )
        response = response.json()
        self.assertEqual(response['code'], 'user_not_found')
