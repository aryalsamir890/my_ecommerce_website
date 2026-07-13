from django.shortcuts import render,get_object_or_404,redirect
from products.models import product
from django.http import HttpResponse
from products.forms import productform
from django.contrib.auth.decorators import permission_required
from django.contrib import messages

def home(request):
    data=product.objects.all()
    return render(request,'home.html',{'data':data})


def categories(request,cate):
    data=product.objects.filter(category=cate)
    return render(request,'categories.html',{'data':data})


# @permission_required('products.add_product' ,raise_exception=True)
def add_product(request):
    if not request.user.has_perm('products.add_product'):
        messages.error(request,'Only admin and staff members can add products')
        return redirect('home')

    if request.method=='POST':
        form=productform(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    
    else:
        form=productform()
    return render(request,'add_product.html',{'form':form})