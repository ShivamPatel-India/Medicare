from django.contrib import admin
from .models.categories import Categorie
from .models.brands import Brand
from .models.supplements import  Supplement



class AdminCat(admin.ModelAdmin):
    list_display = ['name']

class AdminBrand(admin.ModelAdmin):
    list_display = ['name']

class AdminSupplement(admin.ModelAdmin):
    list_display = ['name','price','category','brand']


# Register your models here.
admin.site.register(Categorie,AdminCat);
admin.site.register(Brand,AdminBrand);
admin.site.register(Supplement,AdminSupplement);
