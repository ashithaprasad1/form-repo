from django.db import models

# Create your models here.
class Employee(models.Model):
    eid=models.IntegerField()
    ename=models.CharField(max_length=30)
    email=models.EmailField()
    edoj=models.DateField()
    edesig=models.CharField(max_length=50)
    eexp=models.FloatField()
    ecompany=models.CharField(max_length=50)
    esal=models.IntegerField()
    def __str__(self):
        return self.ename 