from django.shortcuts import render
from .models import Product
from django_user_agents.utils import get_user_agent

# Create your views here.

def all_products(request):
    """ A View to return all_products page including sorting and queries """

    products = Product.objects.all()

    context = {
        'products': products,
    }

    user_agent = get_user_agent(request)

    if user_agent.is_mobile or user_agent.is_tablet:
        return render(request, 'products/mobile_products.html', context)
    elif user_agent.is_pc:
        return render(request, 'products/products.html', context)
