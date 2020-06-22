from django.shortcuts import render
from . import models
from .models import Person
import csv
from .filters import PersonFilter




def timeline(request):
    personen = models.Person.objects.order_by('position_held_startdate')    #Alle Personendatensätze werden nach Startdatum der Position sortiert - Julika
    myFilter = PersonFilter(request.GET, queryset=personen)
    personen = myFilter.qs

    for person in personen:
        person.jahr = person.position_held_startdate[:4]
        person.position_held_start_EU = (person.position_held_startdate[8:10] + "." + person.position_held_startdate[5:7] + "." + person.position_held_startdate[:4])
        person.position_held_end_EU = (person.position_held_enddate[8:10] + "." + person.position_held_enddate[5:7] + "." + person.position_held_enddate[:4])
        person.birthdayEU = (person.birthday[8:10] + "." + person.birthday[5:7] + "." + person.birthday[:4])
        if person.deathday is not None:
            person.deathdayEU = (person.deathday[8:10] + "." + person.deathday[5:7] + "." + person.deathday[:4])
    jahre = []
    for person in personen:
        if person.jahr not in jahre:
            jahre.append(person.jahr)
        else:
            continue
    jahre.sort()
    firstentry = jahre[0]
    lastentry = jahre[-1]
    context = {
        'personen': personen,
        'myFilter': myFilter,
        'firstentry': firstentry,
        'lastentry': lastentry,
    }
    return render(request, "timeline/timeline_neu.html", context)


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






