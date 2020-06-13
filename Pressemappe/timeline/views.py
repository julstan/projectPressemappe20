from django.shortcuts import render
from . import models
from .models import Person
import csv
import json

#Startseite wird aufgerufen unter localhost:8000#


def timeline(request):
    personen = models.Person.objects.order_by('position_held_startdate')    #Alle Personendatensätze werden nach Startdatum der Position sortiert - Julika
    context = {
        'personen': personen,
    }
    return render(request, "timeline/timeline.html", context)

# from django.core import serializers
# json_serializer = serializers.get_serializer("json")()
# personen = json_serializer.serialize(models.Person.objects.order_by('position_held_startdate'))


def person_detail_view(request):
    person = models.Person.objects.order_by('position_held_startdate')
    # context = {
    #     'name' :  obj.name,
    #     'birthday' : obj.birthday,
    #     'deathday'  : obj.deathday,
    #     'position_held' : obj.position_held,
    #     'position_held_startdate' : obj.position_held_startdate,
    #     'position_held_enddate' : obj.position_held_enddate,
    #     'picture' : obj.picture,
    # }
    context = {
        'person': person,
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

# def deutschland_filter ():
#      person = models.Person.objects.filter(name='Deutschland')
#      context = {
#         'person': person,
#      }
#      return render(request, "timeline/deutschland.html", context)
