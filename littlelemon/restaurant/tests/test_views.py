from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer
from rest_framework.test import APIClient
from rest_framework import status


# Create your tests here.
class MenuViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        """Create a user and some menus for testing"""
        # Create a user for testing
        cls.user = User.objects.create_user(
            username="testuser", password="testpassword")
        # Create some menus for testing
        cls.menu = Menu.objects.create(
            Title="IceCream", Price=80, Inventory=100)
        cls.menu2 = Menu.objects.create(
            Title="Pasta", Price=100, Inventory=100)

    def setUp(self):
        # Authenticate the user
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_getall(self):
        response = self.client.get(reverse('menu-list'))
        menus = Menu.objects.all()
        serializer = MenuSerializer(menus, many=True)

        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
