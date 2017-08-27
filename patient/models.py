from django.urls import reverse
from django.db import models
from  datetime import date
from django.contrib.auth.models import User



class Bloodgroup(models.Model):
    bloodgroupId = models.AutoField(primary_key=True)
    bloodgroupDetails = models.CharField(max_length=100)
    bloodgroupType = models.CharField(max_length=10, default='+')

    def __str__(self):
        return  str(str(self.bloodgroupId) + '-' + self.bloodgroupDetails + '-' + self.bloodgroupType )
    def get_absolute_url(self):

       """
    #    Returns the url to access a particular book instance.
    #    """
     #   return reverse('patient:bloodgroup-list')

class Meta:
    managed = True # table creating by django
    #db_table = 'bloodgroup'

class City(models.Model):
    cityid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return str(self.cityid) + '-' + self.name


class Meta:
    managed = True # table creating by django
    #db_table = 'city'

class Patient(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    bloodgroupId = models.ForeignKey('Bloodgroup', models.DO_NOTHING, db_column='bloodgroupid')
    cityid = models.ForeignKey('City', models.DO_NOTHING, db_column='cityid')

    def __str__(self):
        return  str(str(self.id) + '-' + self.name + str(self.bloodgroupId) )
    def get_absolute_url(self):

    #    """
    #    Returns the url to access a particular book instance.
    #    """
        return reverse('patient:bloodgroup-detail' , args=[self.bloodgroupId_id] )

class Meta:
    managed = True
    #db_table = 'patient'






