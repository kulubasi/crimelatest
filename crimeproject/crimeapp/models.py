from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

# Create your models here.

class User(AbstractUser):
    subcounty = models.CharField(max_length = 200,)
    district = models.CharField(max_length = 200, )
    dutystation = models.CharField(max_length = 200)
    contact = models.CharField(max_length = 200)
    is_admin=models.BooleanField('Is admin', default=False)
    is_police_officer=models.BooleanField('Is Police Officer', default=False)
    is_court_Officer=models.BooleanField('Is Court Officer', default=False)

class officers(models.Model):
        # fields of the model
    title=models.CharField(max_length=100)
    firstname = models.CharField(max_length = 200)
    lastname = models.CharField(max_length = 1000)
    dutystation = models.DateTimeField(auto_now_add = True)
    # img = models.ImageField(upload_to = "images/")
  
        # renames the instances of the model
        # with their title name
    def __str__(self):
        return self.title

class Reported(models.Model):
        # fields of the model
    Reference_Number= models.CharField(max_length = 100, blank = True, unique = True,
   default = uuid.uuid4)
    title = models.CharField(max_length = 200, null=True)
    description = models.CharField(max_length = 1000)
    personreported=models.CharField(max_length=100)
    tribe=models.CharField(max_length=100)
    Telephone_Number=models.CharField(max_length=100)
    Residence=models.CharField(max_length=100)
    Officerincharge=models.CharField(max_length=100, blank=True)
    last_modified = models.DateTimeField(auto_now_add = True)
    Status=models.CharField(max_length=5000 ,blank=True)
    CourtStatus=models.CharField(max_length=5000 ,blank=True)
    CrimeScene=models.CharField(max_length=100, blank=True)
    # Penalty=models.CharField(max_length=5000 ,blank=True)


    def __str__(self):
        return self.title


class Forwarded2Court(models.Model):
        # fields of the model
    Reference_Number= models.CharField(max_length = 100, blank = True)
    title = models.CharField(max_length = 200)
    description = models.CharField(max_length = 1000)
    personreported=models.CharField(max_length=100)
    tribe=models.CharField(max_length=100)
    Telephone_Number=models.CharField(max_length=100)
    Residence=models.CharField(max_length=100)
    Officerincharge=models.CharField(max_length=100, blank=True)
    last_modified = models.DateTimeField(auto_now_add = True)
    Status=models.CharField(max_length=5000 ,blank=True)
    CrimeScene=models.CharField(max_length=100, blank=True)
    Penalty=models.CharField(max_length=5000 ,blank=True)


    def __str__(self):
        return self.title