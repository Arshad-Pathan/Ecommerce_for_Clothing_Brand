from django.db import models

#Create your models here.
class Product(models.Model):
  
  
  name = models.CharField(default="", max_length=60)
  
  #pr_images = models.ImageField(blank=True, upload_to=products/)
  
  price = models.DecimalField(default="990", max_digits=10, decimal_places=2)

  #category selection
  Categories = (
    ("Winter Collection","Winter Collection"),
    ("Summer Collection","Summer Collection"),
  )
  
  category = models.TextField(blank=False, choices=Categories)

  #detail & description
  details = models.TextField(default="", max_length=200)
  
  description = models.TextField(default="", max_length=300)
  
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
  
  