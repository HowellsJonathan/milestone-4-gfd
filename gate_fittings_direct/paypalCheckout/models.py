from django.db import models
from django.contrib.auth.models import User
from products.models import Product

# Create your models here.


class Customer(models.Model):
    user = models.OneToOneField(
        User,
        null=True,
        blank=True,
        on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True, blank=True)
    email = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class TotalOrder(models.Model):
    customer = models.ForeignKey(
        Customer,
        on_delete=models.SET_NULL,
        null=True,
        blank=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    order_id = models.CharField(max_length=32, null=True, blank=True)

    def __str__(str):
        return str(self.id)


class OrderItem(models.Model):
    product = models.ForeignKey(
        Product,
        null=True,
        blank=False,
        on_delete=models.SET_NULL)
    order = models.ForeignKey(
        TotalOrder,
        null=True,
        blank=False,
        on_delete=models.SET_NULL)
    quantity = models.IntegerField(null=False, blank=False, default=0)
    lineitem_total = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        null=False,
        blank=False,
        editable=False)
    date_added = models.DateTimeField(auto_now_add=True)


class ShippingAddress(models.Model):
    customer = models.ForeignKey(
        Customer,
        on_delete=models.SET_NULL,
        null=True,
        blank=True)
    order = models.ForeignKey(
        TotalOrder,
        null=False,
        blank=False,
        on_delete=models.CASCADE,
        related_name='lineitems')
    address1 = models.CharField(max_length=80, null=False, blank=False)
    address2 = models.CharField(max_length=80, null=False, blank=False)
    city = models.CharField(max_length=80, null=False, blank=False)
    county = models.CharField(max_length=80, null=False, blank=False)
    postcode = models.CharField(max_length=80, null=False, blank=False)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address1
