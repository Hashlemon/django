from django.db import models
import datetime

class Sensor(models.Model):
    gpio = models.CharField(max_length=2)
    info = models.CharField(max_length=200)

    def __str__(self):
        return self.info

class Data(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)
    temperature = models.FloatField(default=0)
    humidity = models.FloatField(default=0)
    datestamp = models.DateTimeField(auto_now=True)

