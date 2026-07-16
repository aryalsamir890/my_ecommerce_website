from django.shortcuts import render,get_object_or_404,redirect
from .models import product,reviews
from . forms import reviewform
from cart.models import cart
from django.contrib.auth.decorators import login_required



def details(request,id):
    data=get_object_or_404(product,id=id)
    reviewdata=reviews.objects.filter(pname=data)
    return render(request,'product_detail.html',{'data':data,'reviewdata':reviewdata})

@login_required
def review(request,name,id):
    proname=get_object_or_404(product,name=name)
    if request.method=='POST':
        form=reviewform(request.POST)
        if form.is_valid():
            data=form.save(commit=False)
            data.user=request.user
            data.pname=proname
            data.save()
    return redirect('details',id=id)