from django.db import models

class Condition(models.Model):
    condition_name=models.CharField(max_length=400)
    overview=models.TextField(max_length=1000)
    symptoms=models.TextField(max_length=1000)
    causes=models.TextField(max_length=1000)
    complications=models.TextField(max_length=1000)

    def __str__(self):
        return self.condition_name