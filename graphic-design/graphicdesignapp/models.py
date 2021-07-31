from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Design(models.Model):
    name = models.CharField(max_length=255, blank=True)
    image = models.CharField(max_length=255, blank=True)
    category = models.CharField(max_length=80)
    description = models.TextField(blank=True)
    price = models.IntegerField(default=0)
    # created_at = models.DateTimeField(auto_created=True)
    # updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name + " " + str(self.id)


class Order(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, default=0)
    design_id = models.IntegerField()
    category = models.CharField(max_length=80)
    size = models.CharField(max_length=80, blank=True)
    description = models.CharField(
        max_length=255, default='This is Description')
    price = models.IntegerField(default=0)
    is_paid = models.BooleanField(default=False)
    paid_at = models.DateTimeField()
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user.username)
