from django.db import models
from .categories import Categorie
from .brands import Brand


class Supplement(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(decimal_places=2, max_digits=500)
    display_info = models.TextField(max_length=200, default='')
    description = models.TextField(max_length=1000, default='', null=True, blank=True)
    image_1 = models.ImageField(upload_to='Supplements/img', max_length=100, default='default.jpg',null=True,blank=True)
    image_2 = models.ImageField(upload_to='Supplements/img', max_length=100, default='default.jpg',null=True,blank=True)
    image_3 = models.ImageField(upload_to='Supplements/img', max_length=100, default='default.jpg',null=True,blank=True)
    ingredients=models.TextField(max_length=1000,null=True,blank=True)
    benefits=models.TextField(max_length=1000,null=True,blank=True)
    offer = models.DecimalField(decimal_places=2, max_digits=100, default=0.0, null=True, blank=True)
    direction = models.TextField(max_length=1000,null=True,blank=True)
    status = models.BooleanField(default=True)
    category = models.ForeignKey(Categorie, on_delete=models.CASCADE, default=1)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.name