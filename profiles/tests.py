from django.test import TestCase, SimpleTestCase
from django.urls import reverse, resolve
from .views import profile, order_history

""" Url Testing """

class TestUrls(SimpleTestCase):

    def test_profile_resolves(self):
        url = reverse('profile')
        self.assertEqual(resolve(url).func, profile)

    def test_order_history_resolves(self):
        url = reverse('order_history', args='1')
        self.assertEqual(resolve(url).func, order_history)

