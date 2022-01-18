from rest_framework.test import APITestCase, APIClient
from django.urls import reverse

class TestSetUp(APITestCase):
    
    def setUp(self):
        self.register_url = reverse('register')
        self.register_url = reverse('login')

        self.user_data = {
            'email':'email@gmail.com',
            'username':'123',
            'password':'password@1'
        }
        return super().setUp()
    
    def tearDown(self):
        return super().tearDown()

