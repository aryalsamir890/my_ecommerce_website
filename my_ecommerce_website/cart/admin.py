from django.contrib import admin
from . models import cart


class cartadmin(admin.ModelAdmin):
    list_display=['name','proname','quantity']

admin.site.register(cart,cartadmin)