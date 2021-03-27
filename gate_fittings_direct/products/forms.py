from django import forms
from .models import Product, main_category, sub_category


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        main_categories = main_category.objects.all()
        sub_categories = sub_category.objects.all()
        main_friendly_names = [(c.id, c.get_friendly_name()) for c in main_categories]
        sub_friendly_names = [(c.id, c.get_friendly_name()) for c in sub_categories]

        self.fields['main_category'].choices = main_friendly_names
        self.fields['sub_category'].choices = sub_friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'