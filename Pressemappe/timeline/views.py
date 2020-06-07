from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from . import models
from .models import Person
import csv,io
# Create your views here.

#Startseite wird aufgerufen unter localhost:8000#


#def test (request):
    #load_data()
 #   return render(request, "timeline/timeline.html")
#def test(request):
    #return HttpResponse(Person.objects.all())

def timeline(request):
    personen = models.Person.objects.order_by('position_held_startdate')    #Alle Personendatensätze werden nach Startdatum der Position sortiert - Julika
    alledatums = []
    for person in personen:
        datum = person.position_held_startdate
        if datum[:4] not in alledatums:
            alledatums.append(datum[:4])
            person.jahr = datum[:4]
        elif datum[:4] in alledatums:
            person.jahr = None
        else:
            person.jahr = '????????????????????????????'
    context = {
        'personen': personen,
    }
    return render(request, "timeline/timeline.html", context)


def person_detail_view(request):
    person = models.Person.objects.order_by('position_held_startdate') #ergiebt mehr Sinn das nach Startdatum zu sortieren oder? Julika
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

#TODOS
#Alle Datensätze holen -----glaub fertig Patty
#Datensätze sortieren   -----glaub fertig Patty, ka nach was man sortiert
#Daten in der Timeline Struktur mit Schleife anzeigen lassen (Template)  --Daten sind da, noch Jahre ausgeben lassen
#evtl. Funktionen ausdenken, Fehler beheben

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
            person.save()
