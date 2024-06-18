from django.test import TestCase, Client
from django.urls import reverse

class TestHomeView(TestCase):
    def setUp(self):
        self.client = Client()

    def test_home_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
    
    def test_home_view_template(self):
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'home/home.html')
    
    def test_home_view_substance(self):
        response = self.client.get(reverse('home'))
        self.assertContains(response, 'Always Homemade')
        self.assertContains(response, 'Paradise For Pasta Lovers By Pasta Lovers')
        self.assertContains(response, 'Famiglia Mutatio')
        self.assertContains(response, 'Come Get A Taste Of Old Italy At Mutatios')
