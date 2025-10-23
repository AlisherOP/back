from django.db import models

# Create your models here.
# to mig
# to edite  the list you should first:(Item.objects.all() for checking the insides)
#1python manage.py shell then from food.models import Item. To creat objects
#t00rsh04, user:tursh, gmail: tursh04
class Item(models.Model):

    def __str__(self):
        return self.item_name 

    item_name= models.CharField(max_length=200)
    item_desc= models.CharField(max_length=200)
    item_price=models.IntegerField()
    item_image = models.CharField(max_length=500 , default="https://cdn.dribbble.com/userupload/22570626/file/original-379b4978ee41eeb352e0ddacbaa6df96.jpg")