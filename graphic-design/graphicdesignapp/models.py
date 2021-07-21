from django.db import models

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=80, unique=True)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "user"
