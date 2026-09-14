from django.contrib import admin
from .models import *

# Register your Models here
@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
  list_display = ['Collection_name']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
  list_display = ['name', 'price']
  list_filter = ['category', "name"]
