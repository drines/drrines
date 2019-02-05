from django.db import models

# Create your models here.
class Signal(models.Model):
    active = models.BooleanField(default=True)
    title = models.CharField(max_length=100)