from django.db import models

# Create your models here.

class StudentSearch(models.Model):
    query = models.CharField(max_length=100)
