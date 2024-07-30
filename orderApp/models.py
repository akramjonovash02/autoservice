from django.db import models
from mainApp.models import *
from userApp.models import *

class OrderProduct(models.Model):
    STATUS_CHOICES = (
        ('1', 'confirmate is pending'),
        ('2', 'is being collected'),
        ('3', 'is being delivered'),
        ('4', 'successfully'),
        ('5', 'canceled'),
    )
    PAYMENT_CHOICES = (
        ('CASH', 'CASH'),
        ('CARD', 'CARD')
    )

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Users, on_delete=models.CASCADE)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES)
    payment_type = models.CharField(max_length=10, choices=PAYMENT_CHOICES)
    order_date = models.DateField(auto_now_add=True)

class OrderService(models.Model):
    STATUS_CHOICES = (
        ('1', 'confirmate is pending'),
        ('2', 'is being collected'),
        ('3', 'is being delivered'),
        ('4', 'successfully'),
        ('5', 'canceled'),
    )
    PAYMENT_CHOICES = (
        ('CASH', 'CASH'),
        ('CARD', 'CARD')
    )

    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    customer = models.ForeignKey(Users, on_delete=models.CASCADE)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES)
    payment_type = models.CharField(max_length=10, choices=PAYMENT_CHOICES)



