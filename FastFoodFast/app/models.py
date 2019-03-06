from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Menu(models.Model):
    food_name = models.CharField(max_length=100)
    price = models.IntegerField()

    def __str__(self):
        return self.food_name


class Order(models.Model):
    quantity = models.IntegerField()
    location = models.CharField(max_length=100)
    status = models.CharField(max_length=100)

    def __str__(self):
        return self.status
