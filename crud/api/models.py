from django.db import models

# Create your models here.
class Student(models.Model):
    id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=20)
    classname=models.CharField(max_length=10)
    
   