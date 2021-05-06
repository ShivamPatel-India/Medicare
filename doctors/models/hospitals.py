from django.db import models

class Hospital(models.Model):
    hospital_name=models.CharField(max_length=400)
    address=models.TextField(max_length=500,default="")
    contact_no=models.BigIntegerField(default=0)

    def __str__(self):
        return self.hospital_name