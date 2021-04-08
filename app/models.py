from django.db import models
from django.contrib.auth.models import User

class Beer(models.Model):
    Manufacturer = models.CharField(max_length=100) #Завод производитель
    Price = models.FloatField(default=0) #Цена
    Beer_name = models.CharField(max_length=100) #Наименование пива
    Photo = models.ImageField() #это для картинок

class Cart(models.Model):
    User = models.ManyToManyField(Beer)

class Characteristic(models.Model):
    Style = models.CharField(max_length=100) #Это ии (Ale) или (Lager), также смешанный (Mixed)
    ABV = models.FloatField(default=0) #ABV – Alcohol by Volume – показатель крепости пива.
    IBU = models.IntegerField(default=0) #International Bitterness Unit – международная единица горькости
    OG = models.FloatField(default=0) #OG – Original Gravity начальная плотность пива




# class Client(models.Model):
#     address = models.CharField(max_length=100)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)



# Create your models here.
# python manage.py migrate app


