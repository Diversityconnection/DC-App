from django.db import models


class Country(models.Model):
    class Meta:
        verbose_name = "Country"
        verbose_name_plural = "Countries"

    title = models.CharField(max_length=128)

    def __str__(self):
        return self.title


class City(models.Model):
    class Meta:
        verbose_name = "City"
        verbose_name_plural = "Cities"

    title = models.CharField(max_length=128)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
