from django.db import models

# Create your models here.

class Netflix(models.Model):
    photo = models.URLField()
    qualification = models.IntegerField()
    title = models.CharField(max_length=300)

class Prime(models.Model):
    photo = models.URLField()
    qualification = models.IntegerField()
    title = models.CharField(max_length=300)
    
class HBO(models.Model):
    photo = models.URLField()
    qualification = models.IntegerField()
    title = models.CharField(max_length=300)

class Disney(models.Model):
    photo = models.URLField()
    qualification = models.IntegerField()
    title = models.CharField(max_length=300)