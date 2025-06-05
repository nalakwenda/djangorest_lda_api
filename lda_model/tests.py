from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

class LDATopicAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = reverse('classify-text')

    def test_classify_text(self):
        response = self.client.post(self.url, {"text": "The economy is booming with tech jobs"}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("topics", response.data)
        self.assertTrue(len(response.data["topics"]) > 0)