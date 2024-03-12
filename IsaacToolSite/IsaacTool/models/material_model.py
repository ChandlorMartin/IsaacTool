from django.db import models


class Material(models.Model):
    name = models.CharField(max_length=20)
    #C^-1
    linear_coefficient = models.DecimalField(decimal_places=10, max_digits=10)
    volumetric_coefficient = models.DecimalField(decimal_places=10, max_digits=10)

    def __str__(self):
        return self.name
