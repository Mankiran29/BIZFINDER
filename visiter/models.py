from django.db import models
from django.core.validators import RegexValidator

class Member(models.Model):
    name=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
    firstName=models.CharField(max_length=20,null=True)
    lastName=models.CharField(max_length=20,null=True)
    addressM=models.CharField(max_length=20,null=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phoneM = models.CharField(validators=[phone_regex], blank=True,max_length=15,null=True)
    emailM=models.EmailField(null=True)
    
    
    def __iter__(self):
        return [ self.name, 
                 self.firstName, 
                 self.lastName, 
                 self.addressM, 
                 self.phoneM, 
                 self.emailM, 
                  ] 


class Registration(models.Model):
    name=models.CharField(max_length=20,null=True)
    prName=models.CharField(max_length=20,null=True)
    email=models.EmailField(null=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone = models.CharField(validators=[phone_regex], blank=True,max_length=15,null=True) # validators should be a list
    address=models.CharField(max_length=20,null=True)
    city=models.CharField(max_length=20,null=True)
    category=models.CharField(max_length=20,null=True)
    status=models.CharField(max_length=20,null=True)
    
    def __str__(self):
        return self.name


    
    