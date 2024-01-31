from django.db import models

# Create your models here.
class User(models.Model):
    Name=models.CharField(max_length=20)
    Age=models.IntegerField(default=18)
    subject=models.CharField(max_length=15)
    