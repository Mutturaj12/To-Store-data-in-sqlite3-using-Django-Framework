from django.db import models

# Create your models here.
class pysp(models.Model):
    sid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    mobile = models.IntegerField()
    email = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    