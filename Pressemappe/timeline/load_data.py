'''from .models import Person

import csv

with open("../../staatsoberhaupt_filter_test.csv") as csvdatei:
    reader = csv.DictReader(csvdatei, delimiter=",")
    for row in reader:
        Person.pm20id = row ["pm20id"]
        Person.wikidata_object = row ["wikidata_object"]
        Person.name = row ["name"]
        Person.birthday = row ["birthday"] [:10]
        if row ["deathday"] != "":
            Person.deathday = row ["deathday"] [:10]
        Person.position_held = row ["position_held"]
        Person.position_held_startdate = row ["position_held_startdate"] [:10]
        Person.position_held_enddate = row ["position_held_enddate"] [:10]
        if row ["picture"] != "":
            Person.picture = row ["picture"]
        Person.country = row ["countryLabel"]
#        Person.save ()
'''

