from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from . import models
from .models import Person
import csv,io
# Create your views here.

#Startseite wird aufgerufen unter localhost:8000#


def test (request):
    #load_data()
    return render(request, "timeline/timeline.html")
#def test(request):
    #return HttpResponse(Person.objects.all())



def person_detail_view(request):
    person = models.Person.objects.order_by('birthday')
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
        'person' : person,
    }
    return render(request, "timeline/timeline.html", context)

#TODOS
#Alle Datensätze holen -----glaub fertig Patty
#Datensätze sortieren   -----glaub fertig Patty, ka nach was man sortiert
#Daten in der Timeline Struktur mit Schleife anzeigen lassen (Template)
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





