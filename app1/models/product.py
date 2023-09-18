from django.db import models
from .category import Category

class Product(models.Model):
    name = models.CharField(max_length = 100)
    price = models.IntegerField()
    catogory = models.ForeignKey(Category, on_delete= models.CASCADE, default = 1)
    description = models.CharField(max_length = 500, null = True, default = "", blank = True)
    image = models.ImageField(upload_to = 'media/')


