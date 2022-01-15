from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


"""
Guest booking
"""


class Guest(models.Model):
    name = models.CharField(max_length=100, default="", unique="True")
    email = models.EmailField(max_length=200, unique="True")

    def __str__(self):
        return self.name


"""
How many people booking
"""


class Size(models.Model):
    numbers = models.IntegerField()

    def __str__(self):
        return str(self.numbers)


"""
Manage the reservation on the table considering sizes
"""


class Table(models.Model):
    persons = models.IntegerField()
    free = models.BooleanField(default=True)
    date = models.DateTimeField('reservation date and time')
    guest = models.ForeignKey(Guest, on_delete=models.CASCADE, name="reserve")
    tablesizes = models.ManyToManyField(Size)
    featured_image = CloudinaryField('image', default='placeholder')

    class Meta:
        ordering = ['date']
    
    def calculate(self, twochairs, fourchairs, party):
        """
        Calculate the options depending on guests requirements 
        for chairs with the table,
        where the options are: twochairs, fourchairs tables and party, 
        where guets need to contact restaurant
        """

        if twochairs:
            for chair in chairs(self.tablesizes, 2):
                if self.persons == 2:
                    return 'table is available'
        elif fourchairs:
            if (self.persons > 2) and (self.persons <= 4):
                return 'table is available'
        else:
            if self.persons > 4:
                return 'please contact us'

    def __str__(self):
        return self.guest