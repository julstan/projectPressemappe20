from django.db import models

class Person(models.Model):
    pm20id = models.TextField ()
    wikidata_object = models.URLField ()
    name = models.TextField ()
    birthday = models.TextField ()
    deathday = models.TextField (null = True)
    position_held = models.TextField ()
    position_held_startdate = models.TextField ()
    position_held_enddate = models.TextField ()
    picture = models.TextField (null = True)
        #enthält einen Link zu dem Bild
    gender = models.TextField (null = True)
    religion = models.TextField (default = "-")
    predecessor = models.TextField (null = True)
    successor = models.TextField (null = True)
    #eventuell hier später foreign key
    country = models.TextField ()

    def __str__(self):
        return "{}: {}".format(self.name, self.position_held)
    #def __str__(self):
        #return self.name

#Überlegung: jedem Land die jeweiligen Personen zuordnen
#class Country (models.Model):
#    name = models.TextField ()
        #Name des Landes

