from django.db import models

# Create your models here.
class Registration(models.Model):
   user_id = models.CharField(max_length=200,primary_key=True)
   username = models.CharField(max_length=200)
   password = models.CharField(max_length=200)
   status = models.CharField(max_length=200)
   email = models.CharField(max_length=200)
   contact = models.IntegerField(default=0)
   firstname = models.CharField(max_length=200)
   lastname = models.CharField(max_length=200)


class FileSystem(models.Model):
   users = models.ForeignKey(Registration)
   FID = models.CharField(max_length=200)
   filename = models.CharField(max_length=200)
   path = models.CharField(max_length=200)
   size = models.CharField(max_length=200)
   keywords = models.CharField(max_length=200)