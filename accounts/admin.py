from django.contrib import admin
from .models.customers import Customer
from .models.contactUs import Contact_u

class AdminCustomer(admin.ModelAdmin):
    list_display = ['first_name','last_name','contact_no','email']

class AdminContact(admin.ModelAdmin):
    list_display = ['name','email']

# Register your models here.
admin.site.register(Customer,AdminCustomer);
admin.site.register(Contact_u,AdminContact);
