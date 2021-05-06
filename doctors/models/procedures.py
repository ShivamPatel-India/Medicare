from django.db import models

class Procedure(models.Model):
    procedure_name=models.CharField(max_length=400)
    overview=models.TextField(max_length=1000)
    why_its_done=models.TextField(max_length=1000)
    risks=models.TextField(max_length=1000)
    results=models.TextField(max_length=1000)

    def __str__(self):
        return self.procedure_name