from django.db import models

#Create your models here.
class Product(models.Model):
  Categories = models.TextChoices("Winter Collection","Summer Collection")
  #Categories = {"Winter Collection","Summer Collection"}
  
  name = models.CharField(max_length=34)
  description = models.TextField(blank=True, max_length=300)
  # pr_images = models.ImageField(blank=True, upload_to=products/)
  category = models.TextField(blank=True, choices=Categories)
  pub_date = models.DateTimeField("date published")
  