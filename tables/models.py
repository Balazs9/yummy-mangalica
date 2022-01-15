from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))


"""
Guest booking
"""


class Guest(models.Model):
    name = models.CharField(max_length=100, default="")
    email = models.EmailField(max_length=200)

    def __str__(self):
        return self.name.get_fullname()


"""
Table / persons view
"""


class Table(models.Model):
    persons = models.IntegerField()
    free = models.BooleanField(default=True)
    date = models.DateTimeField('reservation date and time')
    guest = models.ForeignKey(Guest, on_delete=models.CASCADE, name="reserve")

    def __str__(self):
        guestname = self.guest.get_fullname
        tablenumber = self.persons.free
        bookedtime = self.date
        return guestname + " for " + tablenumber + " at " + bookedtime