from operator import mod, truediv
from pickle import TRUE
from tkinter import CASCADE
from django.db import models
    
# import enum
# from django.contrib.auth.models import User

# Create your models here.

class Features(models.Model):
    # is_child = models.BooleanField(default=False)
    # userId = models.AutoField(primary_key=True,blank=False,null=False)
    userType = models.TextChoices('userType', 'CHILD PARENT')
    firstName = models.CharField(max_length=200)
    lastName = models.CharField(max_length=200)
    user = models.CharField(blank=False, choices=userType.choices, max_length=10)
    parentId = models.ForeignKey('self',blank=True,null=True,on_delete=models.CASCADE)

    # description = models.TextField(null=True, blank=True)
    # parentName = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True)
    address = models.TextField(
        "Address line",
        max_length=1024,null=True,blank=True
    )

    street = models.CharField(
        "Street",
        max_length=20,null=True,blank=True
    )

    city = models.CharField(
        "City",
        max_length=1024,null=True,blank=True
    )

    state = models.CharField(
        "State",
        max_length=20,null=True,blank=True
    )

    zip_code = models.IntegerField(
        "ZIP / Postal code",null=True,blank=True
    )

    def __str__(self):
        return self.firstName


# class Parent(models.Model):
#     P_first_name = models.CharField(max_length=30) 
#     P_last_name = models.CharField(max_length=30)
#     address = models.TextField("Address line",max_length=1024,null=True,blank=True)
#     street = models.CharField("Street",max_length=20,null=True,blank=True)
#     city = models.CharField("City",max_length=1024,null=True,blank=True)
#     state = models.CharField("State",max_length=20,null=True,blank=True)
#     zip_code = models.IntegerField("ZIP / Postal code",default=1,null=True,blank=True)

# class Child(models.Model):
#     C_first_name = models.CharField(max_length=50)
#     C_last_name = models.CharField(max_length=50)
#     parent_name = models.ForeignKey(Parent,on_delete=CASCADE)
