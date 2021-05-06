from django.db import models

class Department(models.Model):
    department_name=models.CharField(max_length=400)

    def __str__(self):
        return self.department_name