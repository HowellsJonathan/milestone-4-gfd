from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm

# Create your views here.

def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51IYB7ZF3sV2TJ2Nw4xnap8D6HJG7Zvmcq8sL0ke4dSXi6NfLtppw2j4nJs0vnXSFHdXKT0nX5BLafedUxDb889el00R4OaUQUD',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)