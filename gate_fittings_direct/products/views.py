from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib import messages
from django.db.models import Q
from django_user_agents.utils import get_user_agent
from django.db.models.functions import Lower

from .models import Product, sub_category, main_category
from .forms import ProductForm

# Create your views here.

def all_products(request):
    """ A View to return all_products page including sorting and queries """

    products = Product.objects.all()
    query = None
    category = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'MainCategory' in request.GET:
            category = request.GET['MainCategory']
            products = products.filter(main_category__name=category)
            category = main_category.objects.filter(name=category)

        if 'SubCategory' in request.GET:
            category = request.GET['SubCategory']
            products = products.filter(sub_category__name=category)
            category = sub_category.objects.filter(name=category)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, ("You didn't enter any search criteria!"))
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(description__icontains=query) | Q(sku__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_category': category,
        'current_sorting': current_sorting,
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


def add_product(request):
    """ Add a product to the store """
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('add_product'))
        else:
            messages.error(request, 'Failed to add product. Please ensure the form is valid.')
    else:
        form = ProductForm()
        
    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)