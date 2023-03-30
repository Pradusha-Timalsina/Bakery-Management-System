from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class Customer(AbstractUser):
    username = models.CharField(unique=True,max_length = 50,null=False, blank=False)
    first_name = models.CharField(max_length=50, null=False)
    last_name = models.CharField(max_length=50, null=False)
    email = models.EmailField(max_length=200, null=False)
    phone_number = models.CharField(max_length=20, null=False) # added this field

    groups = models.ManyToManyField(
        "auth.Group",
        related_name="customer_set",
        blank=True,
        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
        verbose_name="groups",
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission",
        related_name="customer_set",
        blank=True,
        help_text="Specific permissions for this user.",
        verbose_name="user permissions",
    )

    def __str__(self):
        return self.first_name
    

class Product(models.Model):
    name = models.CharField(max_length=200,null=True)
    price = models.FloatField()
    description = models.TextField(max_length=250,null=True)
    image = models.ImageField(null=True,blank=True,upload_to='images/')
    # date = models.DateField(auto_created=True,auto_now_add=True)

    def __str__(self):
        return self.name