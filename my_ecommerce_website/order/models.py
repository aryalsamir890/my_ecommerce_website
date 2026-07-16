from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from products.models import product

class shipping(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=30)
    phone=models.CharField(max_length=10,validators=[RegexValidator(regex=r'^\d{10}$', message="Phone number must be exactly 10 digits.")
])
    address=models.CharField(max_length=50)
    postal_code=models.IntegerField()


class order(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    status=models.CharField(max_length=10,default='nth')
    date=models.DateTimeField(auto_now_add=True)
    origin=models.CharField(max_length=10,default='nth')
    payment_method=models.CharField(max_length=20,default='nth')

    def __str__(self):
        return f"{self.id}"

# one order needs to hold the multiple order so we do have to create the listorder model
class listorder(models.Model):
    order=models.ForeignKey(order,on_delete=models.CASCADE)
    produ=models.ForeignKey(product,on_delete=models.CASCADE)
    quantity=models.IntegerField()

    def prodname(self):
        return self.produ.name

    @property   
    def total(self):
        value=self.quantity*self.produ.price
        return value
