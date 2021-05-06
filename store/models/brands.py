from django.db import models

class Brand(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=200, default='', null=True, blank=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name