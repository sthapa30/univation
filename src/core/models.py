from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class Car(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    year = models.CharField(max_length=10)

    def __str__(self):
        return self.name
