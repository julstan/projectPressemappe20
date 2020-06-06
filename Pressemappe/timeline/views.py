from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from . import models
from .models import Person
# Create your views here.

#Startseite wird aufgerufen unter localhost:8000#


def test (request):
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
