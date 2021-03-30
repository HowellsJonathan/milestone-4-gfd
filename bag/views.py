from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages

from products.models import Product

# Create your views here.


def view_bag(request):
    """ A view to return the shopping bag page """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add an item to a bag """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    # redirect url for when item has been added to bag, to redirect
    # back to same page
    redirect_url = request.POST.get('redirect_url')
    # create or get a bag from the session for the user
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        # update quantity of item if already in bag
        bag[item_id] += quantity
        messages.success(
            request,
            f'Updated { product.name } quantity to {bag[item_id]}')
    else:
        # add item to bag
        bag[item_id] = quantity
        messages.success(request, f'Added { product.name } to your bag')

    # overright bag variable for session
    request.session['bag'] = bag
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """ Adjust an items quantity in the bag """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    # redirect url for when item has been added to bag, to redirect
    # back to same page
    redirect_url = request.POST.get('redirect_url')
    # create or get a bag from the session for the user
    bag = request.session.get('bag', {})

    if quantity > 0:
        bag[item_id] = quantity
        messages.success(
            request,
            f'Updated { product.name } quantity to {bag[item_id]}')
    else:
        bag.pop(item_id)
        messages.success(request, f'Removed { product.name } from your bag')

    # overright bag variable for session
    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    """ Remove an item from the bag """

    try:
        product = get_object_or_404(Product, pk=item_id)
        # redirect url for when item has been added to bag, to redirect
        # back to same page
        redirect_url = request.POST.get('redirect_url')
        # create or get a bag from the session for the user
        bag = request.session.get('bag', {})

        bag.pop(item_id)
        messages.success(request, f'Removed { product.name } from your bag')

        # overright bag variable for session
        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
