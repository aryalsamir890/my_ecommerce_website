from django.db import models
from django.contrib.auth.models import User
import random

def get_random_value():
        return random.random()

class product(models.Model):
    cate=[
        ('E','Electronics'),
        ('M','Makeup items'),
        ('V','Vehicles'),
        ('F','Foods'),
        ('C','Clothes'),
    ]
    name=models.CharField(max_length=20)
    price=models.IntegerField()
    description=models.CharField(max_length=500)
    image=models.ImageField(upload_to='photos/')
    quantity=models.IntegerField()
    category=models.CharField(choices=cate)
    random_order=models.FloatField(default=get_random_value)

    def __str__(self):
        return self.name
    
class reviews(models.Model):
    pname=models.ForeignKey(product,on_delete=models.CASCADE)
    comments=models.CharField(max_length=500)
    user=models.ForeignKey(User,on_delete=models.CASCADE)

    def fname(self):
        return self.user.first_name
    
    def pro_name(self):
        return self.pname.name
    
