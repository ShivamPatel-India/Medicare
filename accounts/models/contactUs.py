from django.db import models
from .customers import Customer

class Contact_u(models.Model):
    name=models.ForeignKey(Customer,on_delete=models.CASCADE,default='')
    email=models.CharField(max_length=100,null=True,blank=True)
    message=models.TextField(max_length=900,null=True,blank=True)
