from django.db import models


class Image(models.Model):
    images = models.ImageField(upload_to="pix")

class Locate(models.Model):
    name= models.CharField(max_length=50)
    location= models.CharField(max_length=200)
    destination= models.CharField(max_length=200)
    depature_date = models.DateTimeField()
    arrival_date = models.DateTimeField()
    price= models.DecimalField(max_digits=8, decimal_places=2)


    def __str__(self):
        return self.name
