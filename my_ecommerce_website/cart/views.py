from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from products.models import product
from .models import cart
from cart.models import cart
from django.contrib.auth.decorators import login_required
from order.models import shipping
from order.models import order,listorder
from django.views.decorators.http import require_POST

def cart_page(request):
    data=cart.objects.all()
    subtotal_price=0
    for i in data:
        price=i.produ.price*i.quantity
        subtotal_price+=price

    total_price=subtotal_price+100
    return render(request,'cart.html',{'data':data,'subtotal_price':subtotal_price,'total_price':total_price})

@require_POST
@login_required
def add_cart(request,id):
    pro=get_object_or_404(product,id=id)
    quantity=int(request.POST.get('quantity'))
    if cart.objects.filter(user=request.user,produ=pro).exists():
        cart_item=get_object_or_404(cart,produ=pro,user=request.user)
        cart_item.quantity+=quantity
        cart_item.save()
        messages.success(request,'the item has been updated sucessfully!!')
    else:
        cart.objects.create(user=request.user,produ=pro,quantity=quantity)
        messages.success(request,'the item has been placed to the cart sucessfully!!')
    return redirect('details',id)


def remove(request,id):
    value=get_object_or_404(cart,id=id)
    value.delete()
    return redirect('cart')

@login_required
def checkout(request):
    data=shipping.objects.filter(user=request.user).first()
    cartdata=cart.objects.all()
    orderins=order.objects.create(user=request.user,status='pending',origin='cart')
    request.session['orderid']=orderins.id
    for i in cartdata:
        listorder.objects.create(order=orderins,produ=i.produ,quantity=i.quantity)
    subtotal=0
    for i in cartdata:
        subtotal+=i.total_price
    total=subtotal+100
    return render(request,'buy.html',{'data':data,'cartdata':cartdata,'subtotal':subtotal,'total':total})