from django.db import models

class Invoice(models.Model):
    full_name = models.CharField(max_length=255)

    def __str__(self):
        return f"Invoice: {self.id}"