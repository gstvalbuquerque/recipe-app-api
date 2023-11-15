"""
Tests for the health check endpoint.
"""
from django.test import TestCase
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APIClient


class HealthCheckTests(TestCase):
    """
    Test the health check endpoint.
    """

    def test_health_check(self):
        """
        Test the health check endpoint.
        """
        url = reverse('health-check')
        client = APIClient()
        response = client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['healthy'], True)
