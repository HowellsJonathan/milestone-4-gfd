from django.test import TestCase, SimpleTestCase
from django.urls import reverse, resolve
from .views import contact 


class TestUrls(SimpleTestCase):

    def test_contact_is_resolved(self):
        url = reverse('contact')
        self.assertEqual(resolve(url).func, contact)


