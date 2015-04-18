from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase

class MovieTest(APITestCase):
    def test_allmovies(self):
        """
        Ensure we can create a new account object.
        """
       
        response = self.client.get('/cheesetheater/movies/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


























# Create your tests here.
