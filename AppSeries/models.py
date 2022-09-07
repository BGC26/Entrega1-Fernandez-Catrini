from django.db import models

# Create your models here.

class HBO(models.Model):
    photo = models.URLField()
    qualification = models.IntegerField()
    title = models.CharField(max_length=300)

class Disney(models.Model):
    photo = models.URLField()
    qualification = models.IntegerField()
    title = models.CharField(max_length=300)