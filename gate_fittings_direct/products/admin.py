from django.contrib import admin
from .models import Product, main_category, sub_category

# Register your models here.
admin.site.register(Product)
admin.site.register(main_category)
admin.site.register(sub_category)
