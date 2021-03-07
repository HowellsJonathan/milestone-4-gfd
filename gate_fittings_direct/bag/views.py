from django.shortcuts import render, redirect

# Create your views here.

def view_bag(request):
    """ A view to return the shopping bag page """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add an item to a bag """

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
        bag[item_id] = quantity

    # overright bag variable for session
    request.session['bag'] = bag
    print(request.session['bag'])
    return redirect(redirect_url)
