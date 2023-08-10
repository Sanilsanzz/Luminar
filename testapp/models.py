from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import User, Permission
# Create your models here.

choices=(
    ('Two','Two'),
    ('Three','Three'),
    ('Four','Four')
)

class vehicle(models.Model,):
    number=models.IntegerField(null=True,blank=True)
    type=models.CharField(max_length=10,choices=choices)
    model=models.CharField(null=True,blank=True,max_length=80)
    description=models.CharField(null=True,blank=True,max_length=1000)




class UserRole(models.Model):
    ROLE_CHOICES = [
        ('SuperAdmin', 'Super Admin'),
        ('Admin', 'Admin'),
        ('User', 'User'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

