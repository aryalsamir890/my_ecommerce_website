from django.shortcuts import render,redirect,get_object_or_404
from . forms import shippingform
from . models import shipping,order,listorder
from cart.models import cart
from django.db.models import F
from django.http import HttpResponse
from products.models import product
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def buy_now(request):
    id=request.session.get('product_id')
    quantity=request.session.get('quantity')
    data=shipping.objects.filter(user=request.user).first()
    prod=get_object_or_404(product,id=id)
    listvalue=order.objects.create(user=request.user,status='pending',origin='buynow')
    listorder.objects.create(order=listvalue,produ=prod,quantity=quantity)
    request.session['orderid']=listvalue.id
    subtotal=(prod.price)*(int(quantity))
    total=subtotal+100
    return render(request,'buy.html',{'prod':prod,'data':data,'quantity':quantity,'subtotal':subtotal,'total':total})

@login_required
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
    return redirect('buy_now')
    
def editdata(request):
    data=get_object_or_404(shipping,user=request.user)
    if request.method=='POST':
        form=shippingform(request.POST,instance=data)
        if form.is_valid():
            form.save()
        else:
            messages.error(request,'enter the valid values properly')
    return redirect('buy_now')

def placeorder(request):
    if request.method=='POST':
        data=shipping.objects.filter(user=request.user).first()
        if data is None:
            messages.error(request,'fill the shipping form first')
            return redirect('buy_now')
        orderid=request.session.get('orderid')
        check_status(request,orderid)
        payment_method=request.POST.get('payment')
        request.session['payment']=payment_method
        return redirect('placeorders')
    return redirect('home')

def check_status(request,orderid):
    data=get_object_or_404(order,id=orderid)
    if data.status=='paid':
        messages.info(request,'the product has been purchased already')
        return redirect('home')

def placeorder_page(request):
    return render(request,'confirm_order.html')
    
def confirm_order(request):
    if request.method=="POST":
        payment=request.session.get('payment')
        orderid=request.session.get('orderid')
        check_status(request,orderid)
        orderdata=order.objects.filter(user=request.user,id=orderid).first()
        orderdata.payment_method=payment
        orderdata.status='paid'
        orderdata.save()
        if orderdata.origin=='buynow':
            quantity=request.session.get('quantity')
            id=request.session.get('product_id')
            product.objects.filter(id=id).update(quantity=F('quantity')-int(quantity))
        elif orderdata.origin=="cart":
            cart.objects.filter(user=request.user).delete()
            ins=listorder.objects.filter(order=orderdata)
            for i in ins:
                product.objects.filter(id=i.produ.id).update(quantity=F('quantity')-i.quantity)
        return redirect("confirm_order_page")
    return render(request,'confirm_order.html')

def confirm_order_page(request):
    value=listorder.objects.filter(order__id=request.session.get('orderid')).first()
    return render(request,'order.html',{'value':value})

@login_required
def order_list(request):
    data=listorder.objects.filter(order__status='paid',order__user=request.user)
    return render(request,'order_list.html',{'data':data})
