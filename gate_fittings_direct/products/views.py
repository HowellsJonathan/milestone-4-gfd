from django.shortcuts import render
from .models import Product

# Create your views here.

def all_products(request):
    """ A View to return all_products page including sorting and queries """

    products = Product.objects.all()

    context = {
        'products': products,
    }

    user_agent = get_user_agent(request)

    if user_agent.is_mobile or user_agent.is_tablet:
        return render(request, 'home/mobile_products.html', context)
    elif user_agent.is_pc:
        return render(request, 'home/products.html', context)
