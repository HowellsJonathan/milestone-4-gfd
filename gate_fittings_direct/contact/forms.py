from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Field
from .models import message

""" class ContactForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()

        self.helper.form_method = 'post'
        self.helper.form_action = '/contact'

        self.helper.add_input(Submit('submit', 'Submit'))
        
    from_email = forms.EmailField(max_length=254)
    subject = forms.CharField(max_length=30)
    message = forms.CharField(max_length=300, widget=forms.Textarea)

 """
class ContactForm(forms.ModelForm):
    class Meta:
        model = message
        fields = ('from_email', 'subject', 'message',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'from_email': 'Email',
            'subject': 'Subject',
            'message': 'Body'
        }

        self.fields['from_email'].label = "Email:"
        self.fields['subject'].label = "Subject:"
        self.fields['message'].label = "Body:"

        self.fields['from_email'].widget.attrs['autofocus'] = True

        for field in self.fields:
            placeholder = f'{placeholders[field]} *'
            self.fields[field].widget.attrs['placeholder'] = placeholder