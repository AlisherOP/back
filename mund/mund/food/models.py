from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    pic=  models.CharField(max_length=500 , default="https://cdn.dribbble.com/userupload/22570626/file/original-379b4978ee41eeb352e0ddacbaa6df96.jpg")
    desc = models.CharField(max_length=100, default="No description so far")
    def __str__(self):
        return self.name
    