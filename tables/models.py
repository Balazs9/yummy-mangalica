from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


"""
Guest booking
"""


class Guest(models.Model):
    guest = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    date = models.DateField()
    time = models.TimeField()


"""
Table / persons view
"""


class Tables(models.Model):
    persons = models.IntegerField()
    twochairs = models.IntegerField()
    fourchairs = models.IntegerField()
    party = models.IntegerField()
    free = models.BooleanField(default=True)
    book = models.ForeignKey(Guest, on_delete=models.CASCADE, name="reserve")

    def __str__(self):
        return (self.persons) + (self.book)