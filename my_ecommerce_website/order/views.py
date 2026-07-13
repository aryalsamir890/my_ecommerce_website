from django.shortcuts import render,redirect,get_object_or_404
from . forms import shippingform
from . models import shipping,order
from cart.models import cart
from django.http import HttpResponse
from products.models import product
from django.contrib import messages
# from django.views.decorators.http import require_POST

def buy_now(request):
    id=request.session.get('product_id')
    quantity=request.session.get('quantity')
    if id is None or quantity is None:
        return redirect('home')
    data=shipping.objects.filter(user=request.user).first()
    prod=get_object_or_404(product,id=id)
    subtotal=(prod.price)*(int(quantity))
    total=subtotal+100
    return render(request,'buy.html',{'prod':prod,'data':data,'quantity':quantity,'subtotal':subtotal,'total':total})

def buy(request,id):
    request.session['product_id']=id
    quantity=request.POST.get('quantity')
    request.session['quantity']=quantity
    return redirect('buy_now')

def filldata(request):  
    
    if request.method=='POST':
        form=shippingform(request.POST)
        if form.is_valid():
            data=form.save(commit=False)
            data.user=request.user
            data.save()
    if request.session.get('checkout')=='check':
        return redirect("checkout")
    return redirect('buy_now')
 
    
def editdata(request):
    data=get_object_or_404(shipping,user=request.user)
    if request.method=='POST':
        form=shippingform(request.POST,instance=data)
        if form.is_valid():
            form.save()
        else:
            messages.error(request,'enter the valid values properly')
    if request.session.get('checkout')=='check':
        return redirect('checkout')   
    return redirect('buy_now')


def placeorder(request):
    if request.method=='POST':
        payment_method=request.POST.get('payment')
        request.session['payment']=payment_method
        return render(request,"confirm_order.html")
    return redirect('home')
    
def confirm_order(request):
    data=shipping.objects.filter(user=request.user).first()
    payment=request.session.get('payment')
    if data is None:
        messages.error(request,'fill the shipping form first')
        return redirect('buy_now')
    # if request.session.get('checkout')=='check':
    #     cartitem=cart.objects.filter(user=request.user)
    #     for i in cartitem:
    #         value=order.objects.create(user=request.user,produ=i.produ,quanti=i.quantity,payment_method=payment)
        # cartitem.delete()
        # request.session['checkout']='done'
        # return render(request,'order.html',{'value':value})
    # if request.session('checkout')=='done':
    #     return redirect('home')
    id=request.session.get('product_id')
    quantity=request.session.get('quantity')
    if id is None or quantity is None:
        messages.info(request, "This order has already been placed ")   
        return redirect('home')
    pro=get_object_or_404(product,id=id)
    
    pro.quantity-=int(quantity)
    pro.save()
    value=order.objects.create(user=request.user,produ=pro,quanti=quantity,status="paid",payment_method=payment)
    request.session.pop('product_id', None)
    request.session.pop('quantity', None)
    return render(request,'order.html',{'value':value})

def order_list(request):
    data=order.objects.all()
    return render(request,'order_list.html',{'data':data})