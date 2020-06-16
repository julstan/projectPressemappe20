from django.shortcuts import render
from . import models
from .models import Person
import csv
from .filters import PersonFilter

#Startseite wird aufgerufen unter localhost:8000#


def timeline(request):
    personen = models.Person.objects.order_by('position_held_startdate')    #Alle Personendatensätze werden nach Startdatum der Position sortiert - Julika
    myFilter = PersonFilter(request.GET, queryset=personen)
    personen = myFilter.qs

    for person in personen:
        jahr = person.position_held_startdate[:4]

        monat = person.position_held_startdate[6:7]
        tag = person.position_held_startdate[8:9]
        position_held_start_EU = (tag + "." + monat + "." + jahr)
        person.jahr.save()
        person.position_held_start_EU.save()
    context = {
        'personen': personen,
        'myFilter': myFilter,
    }
    return render(request, "timeline/timeline.html", context)


def load_data ():
    with open("../staatsoberhaupt_filter_test.csv") as csvdatei:
        reader = csv.DictReader(csvdatei, delimiter=",")
        for row in reader:
            person = Person ()
            person.pm20id = row ["pm20id"]
            person.wikidata_object = row ["wikidata_object"]
            person.name = row ["name"]
            person.birthday = row ["birthday"] [:10]
            if row ["deathday"] != "":
                person.deathday = row ["deathday"] [:10]
            person.position_held = row ["position_held"]
            person.position_held_startdate = row ["position_held_startdate"] [:10]
            person.position_held_enddate = row ["position_held_enddate"] [:10]
            if row ["picture"] != "":
                person.picture = row ["picture"]
            person.country = row ["country"]
            person.gender = row ["gender"]
            if row ["religionLabel"] != "":
                person.religion = row ["religionLabel"]
            if row ["predecessor"] != "":
                person.predecessor = row ["predecessor"]
            if row ["successor"] != "":
                person.successor = row ["successor"]
            person.save()
