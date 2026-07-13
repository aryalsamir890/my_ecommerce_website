from django.urls import path
from . import views 

urlpatterns = [
    path('',views.cart_page,name='cart'),
    path('remove/<int:id>/',views.remove,name='remove'),
    path('checkout/',views.checkout,name='checkout'),
]
