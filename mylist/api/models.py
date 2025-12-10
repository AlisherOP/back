from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

class Note(models.models):
    title= models.CharField(max_length=100)
    content= models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    author= models.ForeignKey(User, on_delete=models.CASCADE, related_name="notes")

    def __str__(self):
        return self.title
    

class Item(models.Model):

    def __str__(self):
        return self.item_name
    user_name = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    item_name = models.CharField(max_length=200)
    item_desc = models.CharField(max_length=200)
    item_cal = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    auther = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="foods")
    item_image = models.CharField(
        max_length=500, default="https://cdn.dribbble.com/userupload/22570626/file/original-379b4978ee41eeb352e0ddacbaa6df96.jpg")
    favourites = models.ManyToManyField(
        User, related_name='favorite', default=None, blank=None
    )
    # once a new item is created we should go straight to the desciption

    def get_absolute_url(self):
        return reverse("api:index", kwargs={"pk": self.pk})
