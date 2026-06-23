from django.db import models

from django.contrib.auth.models import AbstractUser
# Create your models here.
class Room(models.Model):
    ROOM_TYPE = [
        ('suite',"Suite"),
        ("standard","Standard Room"),
        ("deluxe","Deluxe Room")
    ]
    CURRENCY_TYPE=[
        ("USD","USD"),
        ("USD","EUR")
    ]
    name = models.CharField(max_length=100,blank=True,default="")
    type = models.CharField(max_length=100,choices=ROOM_TYPE)
    pricePerNight = models.PositiveBigIntegerField(default=150)
    currency = models.CharField(default="USD",max_length=100,choices=CURRENCY_TYPE)
    maxOcupy = models.IntegerField(default=1)
    description = models.TextField(max_length = 1000)


class RoomImage(models.Model):
    image = models.ImageField(upload_to='room_images/')
    caption = models.CharField(max_length=255,blank=True,null= True)
    room  = models.ForeignKey(Room,on_delete=models.CASCADE,related_name="images")

from django.conf import settings
class OccupyDate(models.Model):
    room  = models.ForeignKey(Room,on_delete=models.CASCADE,related_name="occupyDate")
    dateField = models.DateField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name="booked_dates")
class User (AbstractUser):
    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length =100,default="")
    