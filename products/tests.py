from django.test import TestCase, SimpleTestCase
from django.urls import reverse, resolve
from .views import (
    all_products, product_detail, add_product, edit_product, delete_product
)

""" Url Testing """

class TestUrls(SimpleTestCase):

    def test_all_products_resolves(self):
        url = reverse('products')
        self.assertEqual(resolve(url).func, all_products)

    def test_product_detail_resolves(self):
        url = reverse('product_detail', args='1')
        self.assertEqual(resolve(url).func, product_detail)

    def test_add_product_resolves(self):
        url = reverse('add_product')
        self.assertEqual(resolve(url).func, add_product)

    def test_edit_product_resolves(self):
        url = reverse('edit_product', args='1')
        self.assertEqual(resolve(url).func, edit_product)

    def test_delete_product_resolves(self):
        url = reverse('delete_product', args='1')
        self.assertEqual(resolve(url).func, delete_product)