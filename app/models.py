from django.db import models
from django.contrib.auth.models import User
class Beer(models.Model):
    Manufacturer = models.CharField(max_length=100)
    Price = models.IntegerField(default=0)

class Characteristic(models.Model):
    Style = models.CharField(max_length=100)
    IBU = models.IntegerField(default=0)
    Gravity = models.IntegerField(default=0)

# class Client(models.Model):
#     address = models.CharField(max_length=100)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)



# Create your models here.
# python manage.py migrate app


