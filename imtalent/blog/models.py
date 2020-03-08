from django.db import models
from django.db.models import Model 
# Create your models here.


class Videos(models.Model):
    name = models.CharField(max_length = 100, default='No Name')
    owner = models.ManyToManyField('Users', blank=True)
    likes = models.IntegerField(null=True)
    comments = models.IntegerField(null=True)


class Users(models.Model):
    auto_increment_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length = 100, default='No Name')
    