from django.db import models


# Create your models here.
class Station(models.Model):
        id = models.IntegerField(primary_key=True)
        name = models.CharField(max_length=128, unique=True)
        latitude = models.DecimalField(max_digits=12, decimal_places=9)
        longitude = models.DecimalField(max_digits=12, decimal_places=9)

        def __str__(self):
                return self.name

        def __int__(self):
                return self.id


class Bike(models.Model):
        station = models.ForeignKey(Station, related_name='start')
        number_of_bikes = models.IntegerField()
        time = models.DateTimeField()

        def __str__(self):
                return str(self.id)
