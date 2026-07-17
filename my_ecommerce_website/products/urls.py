from django.urls import path
from . import views 
from cart.views import add_cart
from order.views import buy

urlpatterns = [
    path('',views.details,name='details'),
    path('review/<str:name>/',views.review,name='review'),
    path('categories',views.review,name='review'),
    path('add_to_cart/',add_cart,name='add_to_cart'),
    path('buy/',buy,name='buy'),
]