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
    country = models.TextField ()
    position_held_start_EU = models.TextField(default=0)
    position_held_end_EU = models.TextField(default=0)
    birthdayEU = models.TextField (default = 0)
    deathdayEU = models.TextField (default = 0)
    jahr = models.TextField(default=0, null = True)

    def __str__(self):
        return "{}".format(self.name)



