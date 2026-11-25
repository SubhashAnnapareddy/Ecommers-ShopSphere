from django.urls import path
from .views import *

urlpatterns = [
    path('add_address/',add_address,name='add_address'),
    path('address_list/',address_list,name='address_list'),
    path('update_address/<int:pk>',update_address,name='update_address'),
    path('checkout/',checkout,name='checkout'),
    path('place_order/',place_order,name='place_order'),
    path('order_success/<int:pk>',order_success,name='order_success'),
    path('order_details/<int:pk>',order_details,name='order_details'),
    path('order_history/',order_history,name='order_history')
]