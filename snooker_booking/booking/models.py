from django.db import models
from django.contrib.auth.models import User
from datetime import date


class Player(models.Model):
    username = models.CharField(max_length=30, unique=True)
    mobile_number = models.CharField(max_length=15, unique=True)
    gender = models.CharField(max_length=10)
    first_name = models.CharField(max_length=30, default=None)
    last_name = models.CharField(max_length=30, default=None)
    password = models.CharField(max_length=255, default=None)
    birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.username

    @property
    def age(self):
        today = date.today()
        birth_date = self.birth_date
        if birth_date:
            age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
            return age
        return None
    
class SnookerTable(models.Model):
    TABLE_TYPES = [
        ('standard_premium', 'Standard Premium'),
        ('standard', 'Standard'),
        ('medium', 'Medium'),
    ]

    type = models.CharField(max_length=20, choices=TABLE_TYPES)
    price = models.DecimalField(max_digits=8, decimal_places=2)

class Booking(models.Model):
    user = models.ForeignKey(Player, on_delete=models.CASCADE)
    table = models.ForeignKey(SnookerTable, on_delete=models.CASCADE)
    booked_at = models.DateTimeField(auto_now_add=True)
