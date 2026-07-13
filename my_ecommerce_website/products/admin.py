from django.contrib import admin
from .models import product,reviews

class productadmin(admin.ModelAdmin):
    list_display=['name','price','quantity']


class reviewsadmin(admin.ModelAdmin):
    list_display=['fname','pro_name','comments']

admin.site.register(product,productadmin)
admin.site.register(reviews,reviewsadmin)
