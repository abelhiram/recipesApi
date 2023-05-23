"""test for the django admin notifications"""
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import Client

class AdminSiteTests(TestCase):
    """test for django admin"""

    def setUp(self):
        """create user and client"""
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email='admin@example.com',
            password='testpass123',
        )
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email='user@example.com',
            password='testpass123',
            name='Test User',
        )

    def test_user_list(self):
        """test that users are listed on page"""
        url = reverse('admin:core_user_changelist')
        res = self.client.get(url)
        print(res.json())
        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)
