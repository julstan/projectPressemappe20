from django.db import models
class Person(models.Model):

    pm20idLabdel =models.TextField()
    person = models.TextField()
    personLabel = models.TextField()
    birthday = models.DateTimeField()
    deathday = models.DateTimeField()
    position_heldLabel= models.TextField()
    startdate = models.DateTimeField()
    picture = models.TextField()
    #eventuell hier später forign key
    country = models.TextField()

class Country (models.Model):
    countryName = models.TextField()

# Create your models here.
