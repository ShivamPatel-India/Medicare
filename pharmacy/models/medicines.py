from django.db import models
from .med_categories import Med_Categorie
from .pharmaceuticals import Pharmaceutical


class Med(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(decimal_places=2, max_digits=500)
    display_info = models.TextField(max_length=200, default='')
    description = models.TextField(max_length=1000, default='', null=True, blank=True)
    image_1 = models.ImageField(upload_to='Medicines/img', max_length=5, default='default.jpg')
    image_2 = models.ImageField(upload_to='Medicines/img', max_length=5, default='default.jpg')
    image_3 = models.ImageField(upload_to='Medicines/img', max_length=5, default='default.jpg')
    offer = models.DecimalField(decimal_places=2, max_digits=100, default=0.0, null=True, blank=True)
    uses = models.TextField(max_length=1000)
    side_effects = models.TextField(max_length=1000, null=True, blank=True)
    storage = models.TextField(max_length=700)
    status = models.BooleanField(default=True)
    category = models.ForeignKey(Med_Categorie, on_delete=models.CASCADE, default=1)
    pharma = models.ForeignKey(Pharmaceutical, on_delete=models.CASCADE, default=1)
    constraint = models.BooleanField(default=False)

    def __str__(self):
        return self.name