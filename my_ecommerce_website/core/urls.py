from django.urls import path,include
from . import views 
from cart.views import cart_page

urlpatterns = [
    path('',views.home,name='home'),
    path('details/<int:id>/',include('products.urls')),
    path('order/',include('order.urls')),
    path('accounts_app/',include('accounts.urls')),
    path('categories/<str:cate>',views.categories,name='categories'),
    path('add_product/',views.add_product,name='add_products'),
    path('cart/',include('cart.urls')),
]
