from django.db import models
from django.contrib.auth.models import AbstractUser

class Users(AbstractUser):
    POSITION_CHOICES = [
        ('Employee', 'Employee'),
        ('Customer', 'Customer')
    ]
    GENDER_CHOICE = (
        ('Male', 'Male'),
        ('Female', 'Female')
    )
    position = models.CharField(max_length=20, choices=POSITION_CHOICES)
    phone_number = models.CharField(max_length=13)
    address = models.CharField(max_length=255, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=10, blank=True, null=True, choices=GENDER_CHOICE)
    date_joined = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name}: {self.position}"



