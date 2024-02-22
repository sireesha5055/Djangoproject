from django.db import models

class Emp(models.Model):
    eid = models.IntegerField()
    ename = models.CharField(max_length=255)
    esal = models.DecimalField(max_digits=10, decimal_places=2)  # Example using DecimalField
    eaddress = models.CharField(max_length=255)

class Product(models.Model):
    pid=models.IntegerField()
    pname=models.CharField(max_length=255)
    price=models.IntegerField()
    