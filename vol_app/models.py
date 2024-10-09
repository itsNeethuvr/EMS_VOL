# vol_app/models.py
from django.db import models

class Volunteer(models.Model):
    name = models.CharField(max_length=100, default='Anonymous')  # Volunteer name
    email = models.EmailField(default='example@example.com')  # Volunteer email
    role = models.CharField(max_length=100)  # Role of the volunteer
    shift_start = models.DateTimeField()  # Shift start time
    shift_end = models.DateTimeField()  # Shift end time

    def __str__(self):
        return f'{self.name} - {self.role}'  # Updated to only use name and role

