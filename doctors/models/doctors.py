from django.db import models
from .department import Department
from .hospitals import Hospital
from .procedures import Procedure
from .conditions import Condition
from .city import Citie

class Doctor(models.Model):
    first_name=models.CharField(max_length=200)
    last_name=models.CharField(max_length=200)
    profile_picture=models.ImageField(upload_to='Doctors/profile_img', max_length=500, default='default.jpg',null=True,blank=True)
    department = models.ManyToManyField(Department, default="")
    area_of_focus = models.TextField(max_length=1000)
    bio=models.TextField(max_length=1000)
    city=models.ForeignKey(Citie,on_delete=models.CASCADE,default="")
    hospital=models.ManyToManyField(Hospital,default="")
    education=models.TextField(max_length=1000)
    awards=models.TextField(max_length=1000)
    procedures_performed=models.ManyToManyField(Procedure,default="")
    condition_trated=models.ManyToManyField(Condition,default="")


    def __str__(self):
        return self.last_name
