from django.db import models
from django.utils import timezone


class Address(models.Model):
    name = models.CharField(max_length=255)
    second_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=50)
    email_address = models.CharField(max_length=50)
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField()

    def __str__(self):
        return self.name
