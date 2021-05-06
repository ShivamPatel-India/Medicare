from django.db import models
from accounts.models.customers import Customer
import datetime


class Order(models.Model):
    customer_id = models.ForeignKey(Customer,on_delete=models.CASCADE)
    order_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=90)
    items =models.CharField(max_length=4000)
    email = models.CharField(max_length=111)
    address = models.CharField(max_length=111)
    city = models.CharField(max_length=111)
    state = models.CharField(max_length=111)
    pin_code = models.CharField(max_length=111)
    phone = models.CharField(max_length=111)
    update_desc = models.TextField(max_length=4000)
    total_amount=models.FloatField(default=0.00)
    timestamp = models.DateTimeField(auto_now_add=True, editable=True)