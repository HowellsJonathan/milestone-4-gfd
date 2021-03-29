from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import contactForm
from django.conf import settings

def index(request):
    """ A View to return Index page """

    return render(request, 'home/index.html')


def contact(request):
    """ A view to return contact page """
    if request.method == 'GET':
        form = contactForm()
    else:
        form = contactForm(request.POST)
        if form.is_valid():
            from_email = form.cleaned_data['from_email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, [settings.DEFAULT_FROM_EMAIL])
            except BadHeaderError:
                messages.error(request, 'Invalid header found \
                Please double check your information.')

            return redirect('contact_success')

    return render(request, 'home/contact.html', {'form': form})


def contactSuccess(request):
    """ A view to return contact success page """

    return render(request, 'home/contact_success.html')

