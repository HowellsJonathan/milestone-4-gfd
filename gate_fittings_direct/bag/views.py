from django.shortcuts import render, redirect, reverse, HttpResponse
from django.contrib import messages

from products.models import Product

# Create your views here.

def view_bag(request):
    """ A view to return the shopping bag page """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add an item to a bag """

    product = Product.objects.get(pk=item_id)
    quantity = int(request.POST.get('quantity'))
    # redirect url for when item has been added to bag, to redirect
    # back to same page
    redirect_url = request.POST.get('redirect_url')
    # create or get a bag from the session for the user
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        # update quantity of item if already in bag
        bag[item_id] += quantity
    else:
        # add item to bag
        messages.success(request, f'Added { product.name } to your bag')
        bag[item_id] = quantity

    # overright bag variable for session
    request.session['bag'] = bag
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """ Adjust an items quantity in the bag """

    quantity = int(request.POST.get('quantity'))
    # redirect url for when item has been added to bag, to redirect
    # back to same page
    redirect_url = request.POST.get('redirect_url')
    # create or get a bag from the session for the user
    bag = request.session.get('bag', {})

    if quantity > 0:
        bag[item_id] = quantity
    else:
        bag.pop(item_id)

    # overright bag variable for session
    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    """ Remove an item from the bag """

    try:
        # redirect url for when item has been added to bag, to redirect
        # back to same page
        redirect_url = request.POST.get('redirect_url')
        # create or get a bag from the session for the user
        bag = request.session.get('bag', {})

        bag.pop(item_id)

        # overright bag variable for session
        request.session['bag'] = bag
        return HttpResponse(status=200)
        
    except Exception as e:
        return HttpResponse(status=500)