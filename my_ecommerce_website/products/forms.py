from django import forms
from . models import reviews,product


class reviewform(forms.ModelForm):
    class Meta:
        model=reviews
        fields=['comments']

class productform(forms.ModelForm):
    class Meta:
        model=product
        fields='__all__'
