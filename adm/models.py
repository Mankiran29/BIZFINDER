from django.db import models
from django.core.validators import RegexValidator

class ADMember(models.Model):
    name=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
    emailM=models.EmailField(null=True)
    
    
    def __iter__(self):
        return [ self.name, 
                 self.firstName, 
                 self.lastName, 
                 self.addressM, 
                 self.phoneM, 
                 self.emailM, 
                  ] 


class Categories(models.Model):
    cate=models.CharField(max_length=20,null=True)
    
    def __str__(self):
        return self.cate

    
    