from django.contrib import admin
from . models import shipping,order,listorder


class shippingadmin(admin.ModelAdmin):
    list_display=['user','name','phone','address']

class orderadmin(admin.ModelAdmin):
    list_display=['user','status','date']

class listorderadmin(admin.ModelAdmin):
    list_display=['order','prodname','quantity']

admin.site.register(shipping,shippingadmin)
admin.site.register(order,orderadmin)
admin.site.register(listorder,listorderadmin)
