from django.db import models

# Create your models here.
class demo(models.Model):
    Describtion = models.TextField(max_length=100)
    Demo_location = models.TextField(max_length=100)
