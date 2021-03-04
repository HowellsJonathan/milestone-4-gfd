from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from products import views

urlpatterns = [
    path('', views.all_products, name='products'),
    path('<product_id>', views.product_detail, name='product_detail'),
] 