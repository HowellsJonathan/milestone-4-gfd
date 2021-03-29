from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django_user_agents.utils import get_user_agent
from django.db.models.functions import Lower

from django.core.paginator import Paginator

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
                paginator = Paginator(products, 12)
                page_number = request.GET.get('page')
                page_obj = paginator.get_page(page_number)

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)
            paginator = Paginator(products, 12)
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)

        if 'MainCategory' in request.GET:
            category = request.GET['MainCategory']
            products = products.filter(main_category__name=category)
            category = main_category.objects.filter(name=category)
            paginator = Paginator(products, 12)
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)

        if 'SubCategory' in request.GET:
            category = request.GET['SubCategory']
            products = products.filter(sub_category__name=category)
            category = sub_category.objects.filter(name=category)
            paginator = Paginator(products, 12)
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, ("You didn't enter any search criteria!"))
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(description__icontains=query) | Q(sku__icontains=query)
            products = products.filter(queries)
            paginator = Paginator(products, 12)
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': page_obj,
        'search_term': query,
        'current_category': category,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A View to return a single products details """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)


@login_required
def add_product(request):
    """ Add a product to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to add product. Please ensure the form is valid.')
    else:
        form = ProductForm()
        
    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """ Edit a product in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product. Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """ Delete a product from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))
        
    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products'))