from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail, BadHeaderError
from django.views.generic.edit import FormView
from django.conf import settings

from .forms import ContactForm
from .models import message
from profiles.models import UserProfile


def contact(request):

    if request.method == 'GET':
        if request.user.is_authenticated:
            try:
                profile = UserProfile.objects.get(user=request.user)
                contact_form = ContactForm(initial={
                    'from_email': profile.user.email,
                })
            except UserProfile.DoesNotExist:
                contact_form = ContactForm()
        else:
            contact_form = ContactForm()
    else:
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            from_email = contact_form.cleaned_data['from_email']
            subject = contact_form.cleaned_data['subject']
            message = contact_form.cleaned_data['message']
            try:
                send_mail(
                    subject,
                    message,
                    from_email,
                    [settings.DEFAULT_FROM_EMAIL]
                )
            except BadHeaderError:
                messages.error(request, 'Invalid header found \
                Please double check your information.')

            messages.success(request, 'Message sent!')
            return redirect('contact')

    template = 'contact/contact.html'
    context = {
        'contact_form': contact_form
    }

    return render(request, template, context)
