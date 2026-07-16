from django.shortcuts import render,get_object_or_404,redirect
from products.models import product
from django.http import HttpResponse
from products.forms import productform
from django.contrib.auth.decorators import permission_required
from django.core.paginator import Paginator
from django.contrib import messages
from django.db.models import Q

def home(request):
    data=product.objects.all().order_by('random_order')
    value=page_inator(request,data)
    return render(request,'home.html',{'page_obj':value})

def page_inator(request,data):
    paginator=Paginator(data,8)
    page_number=request.GET.get('page')  # comes from ?page=2 in the URL
    obj=paginator.get_page(page_number)  #data related to that page number
    return obj


def categories(request,cate):
    data=product.objects.filter(category=cate)
    value=page_inator(request,data)
    return render(request,'categories.html',{'data':value})

def search(request):
    query=request.GET.get('query')
    if len(query)>=20:
        result=[]
    else:
        result=product.objects.filter(Q(name__icontains=query))
        value=page_inator(request,result)
    return render(request,'home.html',{'page_obj':value,'query':query})

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