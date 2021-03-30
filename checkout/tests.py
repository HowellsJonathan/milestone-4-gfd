from django.test import TestCase, SimpleTestCase
from django.urls import reverse, resolve
from .views import cache_checkout_data, checkout, checkout_success

""" Url Testing """

class TestUrls(SimpleTestCase):

    def test_cache_checkout_resolves(self):
        url = reverse('cache_checkout_data')
        self.assertEqual(resolve(url).func, cache_checkout_data)

    def test_checkout_resolves(self):
        url = reverse('checkout')
        self.assertEqual(resolve(url).func, checkout)

    def test_checkout_success_resolves(self):
        url = reverse('checkout_success', args='1')
        self.assertEqual(resolve(url).func, checkout_success)
