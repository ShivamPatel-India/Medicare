from django.contrib import admin
from .models.doctors import Doctor
from .models.hospitals import Hospital
from .models.procedures import Procedure
from .models.city import Citie
from .models.conditions import Condition
from .models.department import Department

class AdminCity(admin.ModelAdmin):
    list_display = ['city_name']

class AdminCondition(admin.ModelAdmin):
    list_display = ['condition_name']

class AdminDept(admin.ModelAdmin):
    list_display = ['department_name']

class AdminProc(admin.ModelAdmin):
    list_display=['procedure_name']

class AdminHospital(admin.ModelAdmin):
    list_display = ['hospital_name']

class AdminDoctor(admin.ModelAdmin):
    list_display = ['first_name','city']

# Register your models here.
admin.site.register(Citie,AdminCity)
admin.site.register(Condition,AdminCondition)
admin.site.register(Department,AdminDept)
admin.site.register(Procedure,AdminProc)
admin.site.register(Hospital,AdminHospital)
admin.site.register(Doctor,AdminDoctor)
