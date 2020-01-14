from django.db import models

from client.models import Client
from place.models import Country, City


class GuideTour(models.Model):
    owner = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='guide_tours')
    title = models.CharField(max_length=128)
    description = models.TextField()
    duration = models.DurationField()
    price = models.PositiveIntegerField()
    country = models.ForeignKey(Country, on_delete=models.PROTECT, related_name='guide_tours')
    city = models.ForeignKey(City, on_delete=models.PROTECT, related_name='guide_tours')
