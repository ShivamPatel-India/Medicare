from django.contrib import admin
from .models.orders import Order
from .models.prescriptions import Prescription
# Register your models here.


class AdminOrder(admin.ModelAdmin):
    list_display = ['customer_id','order_id','name','timestamp','address','city','state','pin_code','phone']

class AdminPrescription(admin.ModelAdmin):
    list_display = ['customer_id','timestamp','prescription']


admin.site.register(Order,AdminOrder)
admin.site.register(Prescription,AdminPrescription)
