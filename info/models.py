from django.db import models

# Create your models here.
class items(models.Model):
    idno = models.PositiveBigIntegerField()
    name = models.CharField(max_length=100)
    company = models.CharField(max_length=225)
    price = models.IntegerField()
    quantity = models.IntegerField()