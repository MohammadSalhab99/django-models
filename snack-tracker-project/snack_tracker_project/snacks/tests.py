from django.test import TestCase

# Create your tests here.
from urllib import request, response
from django.urls import reverse

class SnackTest(TestCase):
    def test_list_page_status_code(self):
        url = reverse("snacks_list")
        response =self.client.get(url)
        self.assertEqual(response.status_code, 200)
    
    def test_list_page_template(self):
        url = reverse("snacks_list")
        response =self.client.get(url)
        self.assertTemplateUsed(response, "snack_list.html")
        self.assertTemplateUsed(response, "base.html")