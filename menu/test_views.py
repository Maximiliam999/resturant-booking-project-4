from django.test import TestCase, Client
from django.urls import reverse
# Create your tests here.

from django.test import TestCase, Client
from django.urls import reverse

class TestMenuView(TestCase):
    def setUp(self):
        self.client = Client()

    def test_menu_view(self):
        response = self.client.get(reverse('menu'))
        self.assertEqual(response.status_code, 200)
    
    def test_menu_view_template(self):
        response = self.client.get(reverse('menu'))
        self.assertTemplateUsed(response, 'menu/menu.html')

    def test_menu_view_substance(self):
        response = self.client.get(reverse('menu'))
        self.assertContains(response, 'STARTER')
        self.assertContains(response, 'MAIN-COURSE')
        self.assertContains(response, 'DESSERT')
