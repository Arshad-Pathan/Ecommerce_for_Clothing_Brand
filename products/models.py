from django.db import models

#Create your models here.

#Collection
class Collection(models.Model):
  Collection_name = models.TextField(unique=True, blank=False, primary_key=True)
  
  def __str__(self):
    return self.Collection_name

#specific product
class Product(models.Model):
  
  name = models.CharField(unique=True, blank=False, max_length=60)
  
  #pr_images = models.ImageField(blank=True, upload_to=products/)
  
  price = models.DecimalField(blank=False, max_digits=10, decimal_places=2)

  #category selection
  category = models.ManyToManyField(Collection, blank=True)

  #detail & description
  details = models.TextField(blank=False, max_length=200)
  
  description = models.TextField(blank=False, max_length=300)
  
  #washcare detail
  COTTON_501 = "this is cotton 501 washcare tips"
  NYLON = "this is Nylon washcare tips"
  
  Washcare_tips = (
    (COTTON_501, "COTTON 501"),
    (NYLON, "NYLON"),
  )

  washcare = models.TextField(default="hii", choices=Washcare_tips)
  
  #shipping detail
  shipping_policy = "read this before shipping"

  shipping = models.TextField(default=shipping_policy)
  
  pub_date = models.DateTimeField("date published")
  
  def __str__(self):
    return self.name