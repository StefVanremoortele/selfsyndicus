from django.db import models
from syndicus.users.models import BaseUser

class Building(models.Model):
    address = models.CharField(max_length=255)
    name = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.address

class Privative(models.Model):
    building = models.ForeignKey(Building, related_name='privatives', on_delete=models.CASCADE)
    name = models.CharField(max_length=255, blank=True, null=True)
    area = models.DecimalField(max_digits=10, decimal_places=2)
    owner = models.ForeignKey(BaseUser, related_name='privatives', on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name
