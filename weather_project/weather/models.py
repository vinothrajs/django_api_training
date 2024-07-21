from django.db import models

# Create your models here.
class Weather(models.Model):
    city = models.CharField(max_length=100)
    temperature = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.city} - {self.temperature}"