from django.db import models

class Person(models.Model):
    pm20id = models.TextField ()
    wikidata_object = models.TextField ()
    name = models.TextField ()
    birthday = models.TextField ()
    deathday = models.TextField (null = True)
    position_held = models.TextField ()
    position_held_startdate = models.TextField ()
    position_held_enddate = models.TextField ()
    picture = models.TextField (null = True)
        #enthält einen Link zu dem Bild
    #eventuell hier später foreign key
    country = models.TextField ()

    def __str__(self):
        return "{}: {}".format(self.name, self.position_held)


#Überlegung: jedem Land die jeweiligen Personen zuordnen
#class Country (models.Model):
#    name = models.TextField ()
        #Name des Landes

