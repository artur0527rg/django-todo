from django.urls import reverse
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Group, ToDo


User = get_user_model()


class ToDoTests(APITestCase):
    def setUp(self) -> None:
        user1 = {
            'username': 'user1',
            'password': 'user1',
            'email' : 'user1@gmail.com',
        }
        user2 = {
            'username': 'user2',
            'password': 'user2',
            'email' : 'user2@gmail.com',
        }
        self.user1 = User.objects.create(
            username = user1['username'],
            password = make_password(user1['password']),
            email = user1['email'],
            )
        self.user2 = User.objects.create(
            username = user2['username'],
            password = make_password(user2['password']),
            email = user2['email'],
            )
        self.token1 = self.client.post(reverse('token_obtain_pair'), data=user1).json()
        self.token2 = self.client.post(reverse('token_obtain_pair'), data=user2).json()

        self.HEADER_TYPES = 'Bearer '


    def test_anon_user_group(self):
        response = self.client.get(reverse('group-list'))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_anon_user_todo(self):
        response = self.client.get(reverse('todo-list', kwargs={'group_id':'999'}))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_user_create(self):
        response = self.client.get(
            reverse('group-list'),
            headers = {'Authorization': self.HEADER_TYPES + self.token1['access']},
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response = self.client.post(
            reverse('group-list'),
            data = {'title':'test'},
            headers = {'Authorization': self.HEADER_TYPES + self.token1['access']},
        )
        self.assertEqual(
            response.status_code, 
            status.HTTP_201_CREATED, 
            'User can`t create group'
        )

        response = self.client.get(
            reverse('group-list'),
            headers = {'Authorization': self.HEADER_TYPES + self.token1['access']},
        )
        self.assertEqual(len(response.json()), 1, 'The group has not been saved to the model')

        response = self.client.get(
            reverse('group-list'),
            headers = {'Authorization': self.HEADER_TYPES + self.token2['access']},
        )
        self.assertEqual(
            len(response.json()),
            0,
            'The user can view other people`s groups',
        )
        
        response = self.client.post(
            reverse('todo-list', kwargs={'group_id':1}),
            data={'title': 'test'},
            headers = {'Authorization': self.HEADER_TYPES + self.token1['access']},
            )
        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED,
            'User can`t create todo',
        )

        response = self.client.get(
            reverse('todo-list', kwargs={'group_id':1}),
            headers = {'Authorization': self.HEADER_TYPES + self.token1['access']},
            )
        self.assertNotEqual(
            len(response.json()),
            0,
            'The todo has not been saved to the model',
        )

        response = self.client.get(
            reverse('todo-list', kwargs={'group_id':1}),
            headers = {'Authorization': self.HEADER_TYPES + self.token2['access']},
        )
        self.assertNotEqual(
            len(response.json()),
            0,
            'The user can view other people`s todo')