from django.db import models

#Create your models here.
class Product(models.Model):
  Categories = models.TextChoices("Winter Collection", "Summer Collection")
  
  name = models.CharField(max_length=34)
  category = models.CharField(blank=True, max_length=34, choices=Categories)
  pub_date = models.DateTimeField("date published")
  