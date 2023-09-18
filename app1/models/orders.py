from .product import Product
from .category import Category
from .customer import Customer
from django.db import models
import datetime

class Order(models.Model):
    product = models.ForeignKey(Product, on_delete = models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete = models.CASCADE)
    price = models.IntegerField()
    qty = models.IntegerField(default = 1)
    address = models.CharField(max_length = 1000, default = "", blank = True)
    phone = models.CharField(max_length = 15, default = "", blank = True)
    date = models.DateField (default=datetime.datetime.today)
    status = models.BooleanField(default = False)