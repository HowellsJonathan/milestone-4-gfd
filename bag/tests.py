from django.test import TestCase, SimpleTestCase
from django.urls import reverse, resolve
from .views import view_bag, add_to_bag, adjust_bag, remove_from_bag 

""" Url Testing """

class TestUrls(SimpleTestCase):

    def test_view_bag_is_resolved(self):
        url = reverse('view_bag')
        self.assertEqual(resolve(url).func, view_bag)

    def test_add_to_bag_is_resolved(self):
        url = reverse('add_to_bag', args='1')
        self.assertEqual(resolve(url).func, add_to_bag)

    def test_adjust_bag_is_resolved(self):
        url = reverse('adjust_bag', args='1')
        self.assertEqual(resolve(url).func, adjust_bag)

    def test_remove_from_bag_is_resolved(self):
        url = reverse('remove_from_bag', args='1')
        print(resolve(url))


    
