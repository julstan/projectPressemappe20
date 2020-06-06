from django.shortcuts import render, get_object_or_404
from .models import Person
# Create your views here.

#Startseite wird aufgerufen unter http://localhost:8000/timeline/show#

def test(request):
    return render(request,'timeline/template.html')



def person_detail_view(request):
    person = Person.object.order_by(id=1)
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
    return render(request, "timeline/template.html", context)

#TODOS
#Alle Datensätze holen
#Datensätze sortieren
#Daten in der Timeline Struktur mit Schleife anzeigen lassen (Template)
#evtl. Funktionen ausdenken, Fehler beheben
