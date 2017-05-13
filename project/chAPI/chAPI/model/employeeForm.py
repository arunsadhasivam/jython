from unittest.util import _MAX_LENGTH
from django.db import models
 
class employee(models.Model):
     
    name = models.CharField(max_length=10)
    empid = models.CharField(max_length=30)
    employer = models.CharField(max_length=50)
  
   
    def __str__(self):
       return self.name;
 
          
