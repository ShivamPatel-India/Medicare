from django.contrib import admin
from .models.med_categories import Med_Categorie
from .models.pharmaceuticals import Pharmaceutical
from .models.medicines import Med


class AdminCat(admin.ModelAdmin):
    list_display = ['name']

class AdminPharma(admin.ModelAdmin):
    list_display = ['name','status']

class AdminMed(admin.ModelAdmin):
    list_display = ['name','price','category','pharma']



# Register your models here.
admin.site.register(Med_Categorie,AdminCat);
admin.site.register(Pharmaceutical,AdminPharma);
admin.site.register(Med,AdminMed);
