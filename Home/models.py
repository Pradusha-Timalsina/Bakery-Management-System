from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Customer(models.Model):
    user = models.OneToOneField(User,on_delete = models.CASCADE,null=True,blank=True)
    name = models.CharField(max_length=200,null=True)
    email = models.EmailField(max_length=200,null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200,null=True)
    price = models.FloatField()
    description = models.TextField(max_length=250,null=True)
    image = models.ImageField(null=True,blank=True,upload_to='images/')
    # date = models.DateField(auto_created=True,auto_now_add=True)

    def __str__(self):
        return self.name