from django.db import models
from accounts.models.customers import Customer
import datetime


class Prescription(models.Model):
    customer_id = models.ForeignKey(Customer,on_delete=models.CASCADE)
    prescription=models.ImageField(upload_to='Prescriptions/img', max_length=500, default='default.jpg',null=True,blank=True)
    timestamp = models.DateTimeField(auto_now_add=True, editable=True)