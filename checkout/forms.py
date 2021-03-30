from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('full_name', 'email', 'phone_number',
                  'street_address1', 'street_address2',
                  'town_or_city', 'postcode', 'country',
                  'county',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'full_name': 'Full Name',
            'email': 'Email Address',
            'phone_number': 'Phone Number',
            'postcode': 'Postal Code',
            'town_or_city': 'Town or City',
            'street_address1': 'Address',
            'street_address2': 'Address 2',
            'county': 'County',
        }

        self.fields['full_name'].label = "Full Name:"
        self.fields['email'].label = "Email:"
        self.fields['phone_number'].label = "Phone Number:"
        self.fields['postcode'].label = "Postcode:"
        self.fields['town_or_city'].label = "Town / City:"
        self.fields['street_address1'].label = "Address"
        self.fields[
            'street_address2'].label = "Address 2 <small class='text-muted'>(optional)</small>"
        self.fields['county'].label = "County"

        self.fields['full_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
