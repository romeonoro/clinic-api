from django.db import models

class Doctor(models.Model):
    name = models.CharField(max_length=120)
    specialty = models.CharField(max_length=120)
    crm = models.CharField(max_length=20)

    def __str__(self):
        return self.name