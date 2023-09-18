from django.db import models


class Customer(models.Model):
    first_name = models.CharField(max_length = 250)
    last_name = models.CharField(max_length = 250)
    email = models.EmailField(unique = True)
    phone = models.CharField(max_length = 50)
    password = models.CharField(max_length = 1000)