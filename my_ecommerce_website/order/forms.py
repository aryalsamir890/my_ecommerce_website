from django import forms
from . models import shipping



class shippingform(forms.ModelForm):
    class Meta:
        model=shipping
        fields=['name','phone','address','postal_code']
