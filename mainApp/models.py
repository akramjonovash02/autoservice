from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    price = models.FloatField(null=True, blank=True)
    sku = models.CharField(max_length=10)
    stock_quantity = models.PositiveIntegerField()
    manufacturer = models.CharField(max_length=100)
    warranty = models.CharField(max_length=255)

class Image(models.Model):
    images = models.ImageField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

class Service(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
