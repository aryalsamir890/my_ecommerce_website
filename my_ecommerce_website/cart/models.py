from django.db import models
from django.contrib.auth.models import User
from products.models import product

class cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    produ=models.ForeignKey(product,on_delete=models.CASCADE)
    quantity=models.IntegerField()

    @property
    def total_price(self):
        return self.produ.price*self.quantity

    def name(self):
        return self.user.first_name
    
    def proname(self):
        return self.produ.name
