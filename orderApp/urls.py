from django.urls import path

from orderApp.views import OrderProductCreateView, OrderServiceCreateView

urlpatterns = [
    path('order_products/create/', OrderProductCreateView.as_view(), name='order-product-create'),
    path('order_services/create/', OrderServiceCreateView.as_view(), name='order-service-create'),
]