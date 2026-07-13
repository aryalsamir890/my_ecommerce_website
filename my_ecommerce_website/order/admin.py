from django.contrib import admin
from . models import shipping,order


class shippingadmin(admin.ModelAdmin):
    list_display=['user','name','phone','address']


class orderadmin(admin.ModelAdmin):
    list_display=['user','name','date']

admin.site.register(shipping,shippingadmin)
admin.site.register(order,orderadmin)