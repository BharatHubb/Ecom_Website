from django.contrib import admin
from app1.models.category import Category 
from app1.models.product import Product 
# Register your models here.

admin.site.register([Category, Product])