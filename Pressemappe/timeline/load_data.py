from .models import Person

import csv

with open("wikidata_pm20_persons.csv", encoding = "utf-8") as csvdatei:
    reader = csv.DictReader(csvdatei, delimiter=",")
    for row in reader:
        Person.pm20id = row ["pm20idLabel"]
        Person.wikidata_object = row ["person"]
        Person.name = row ["personLabel"]
        Person.birthday = row ["birthday"]
        Person.deathday = row ["deathday"]
        Person.position_held = row ["position_heldLabel"]
        Person.position_held_startdate = row ["start"]
        Person.position_held_enddate = row ["end"]
        Person.picture = row ["picture"]
        Person.country = row ["countryLabel"]
#        Person.save ()

