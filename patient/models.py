from django.urls import reverse
from django.db import models
from  datetime import date
from django.contrib.auth.models import User



class Bloodgroup(models.Model):
    bloodgroupId = models.AutoField(primary_key=True)
    bloodgroupDetails = models.CharField(max_length=100)


    def __str__(self):
        return  str(str(self.bloodgroupId) + '-' + self.bloodgroupDetails  )
    def get_absolute_url(self):
        """
        Returns the url to access a particular book instance.
        """
        return reverse('patient:bloodgroup-list')



class Meta:
    managed = True
    #db_table = 'bloodgroup'

class Patient(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    bloodgroupId = models.ForeignKey('BloodGroup', models.DO_NOTHING, db_column='bloodgroupid')

class Meta:
    managed = True
    #db_table = 'patient'






