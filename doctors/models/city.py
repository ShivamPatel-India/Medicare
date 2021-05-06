from django.db import models

class Citie(models.Model):
    city_name=models.CharField(max_length=400)

    def __str__(self):
        return self.city_name