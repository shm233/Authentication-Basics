from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class customuser(AbstractUser):
    
    city = models.CharField(max_length=100, null=True)
    reg_number = models.IntegerField(null=True)
    
    def __str__(self):
        return f"{self.username}----{self.reg_number}"
