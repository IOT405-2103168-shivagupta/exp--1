from django.db import models

class dht(models.Model):
    temp =models.TextField(max_length=64)
    humd = models.TextField(max_length=64)
    count=models.IntegerField()
    
