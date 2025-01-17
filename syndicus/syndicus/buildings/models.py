from django.db import models
from syndicus.users.models import BaseUser

class Building(models.Model):
    address = models.CharField(max_length=255)
    name = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.address