from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User


class AuthenticationFlowTest(APITestCase):
    def test_register_login_and_access(self):
        register_url = reverse('register')
        data = {
            'username': 'john',
            'email': 'john@example.com',
            'password': 'pass1234'
        }
        res = self.client.post(register_url, data)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

        login_url = reverse('login')
        login_res = self.client.post(login_url, {
            'username': 'john',
            'password': 'pass1234'
        })
        self.assertEqual(login_res.status_code, status.HTTP_200_OK)
        access = login_res.data.get('access')
        self.assertIsNotNone(access)

        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {access}')
        list_url = reverse('course-list')
        resp = self.client.get(list_url)
        self.assertEqual(resp.status_code, status.HTTP_200_OK)

    def test_courses_requires_authentication(self):
        url = reverse('course-list')
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, status.HTTP_401_UNAUTHORIZED)

