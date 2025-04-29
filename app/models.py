from django.db import models
from datetime import date
# Create your models here.
class Consumer(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    contact = models.IntegerField()
    dob = models.DateField()
    gender = models.CharField( max_length=50)
    password = models.CharField( max_length=50)
    # def __str__(self):
    #     return str(self.email)

class Query(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    query=models.CharField(max_length=50)
    # email = models.ForeignKey(Consumer,on_delete=models.PROTECT)