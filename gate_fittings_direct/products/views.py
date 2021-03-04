from django.shortcuts import render, get_object_or_404
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


def product_detail(request, product_id):
    """ A View to return a single products details """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    user_agent = get_user_agent(request)

    if user_agent.is_mobile or user_agent.is_tablet:
        return render(request, 'products/mobile_product_detail.html', context)
    elif user_agent.is_pc:
        return render(request, 'products/product_detail.html', context)