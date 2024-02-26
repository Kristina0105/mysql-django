from django.db import models

class Restaurants(models.Model):
    ITALIAN = 'Italian'
    FRENCH = 'French'
    ASIAN = 'Asian'
    FAMILY = 'Family'
    OTHER = 'Other'

    SPECIALIZATION_CHOICES = [
        (ITALIAN, 'Italian'),
        (FRENCH, 'French'),
        (ASIAN, 'Asian'),
        (FAMILY, 'Family'),
        (OTHER, 'Other'),
    ]

    name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100, choices=SPECIALIZATION_CHOICES)
    address = models.CharField(max_length=200)
    website = models.URLField()
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return self.name