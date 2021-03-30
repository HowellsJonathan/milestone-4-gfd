from django.contrib import admin
from .models import Product, main_category, sub_category

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'main_category',
        'sub_category',
        'price',
        'rating',
        'image',
    )

    ordering = ('sku', )


class Main_categoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


class Sub_categoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
        'main_category',
        'image',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(main_category, Main_categoryAdmin)
admin.site.register(sub_category, Sub_categoryAdmin)
