from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase


class SearchTest(APITestCase):
    def test_search_summary_with_valid_data(self):
        url = reverse('summaries-list')
        data = {"queries": ["is your problems", "achieve take book"], "k": 3}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_search_summary_with_invalid_data(self):
        url = reverse('summaries-list')
        data = {"queries": ["is your problems", "achieve take book"], "k": 'sss'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
