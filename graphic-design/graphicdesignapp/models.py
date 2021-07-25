from django.db import models

# Create your models here.


class Design(models.Model):
    name = models.CharField(max_length=255, blank=True)
    image = models.CharField(max_length=255, blank=True)
    category = models.CharField(max_length=80)
    description = models.TextField(blank=True)
    price = models.CharField(max_length=80)

    def __str__(self):
        return self.name
