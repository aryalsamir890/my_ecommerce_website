from django.urls import path
from . import views 

urlpatterns = [
    path('',views.buy_now,name='buy_now'),
    path('filldata/',views.filldata,name='filldata'),
    path('editdata/',views.editdata,name='editdata'),
    path('confirm/',views.confirm_order,name='confirm_order'),
    path('placeorder/',views.placeorder,name='placeorder'),
    path('placeorders/',views.placeorder_page,name='placeorders'),
    path('order_list/',views.order_list,name='order_list'),
    path('success/',views.confirm_order_page,name='confirm_order_page'),

]