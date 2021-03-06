from django.shortcuts import render
from . import models
from .models import Person
import csv
from .filters import PersonFilter #django-filter





def timeline(request):
    personen = models.Person.objects.order_by('position_held_startdate')    #Alle Personendatensätze werden nach Startdatum der Position sortiert
    myFilter = PersonFilter(request.GET, queryset=personen) #django-filter -> myFilter erhält die einzelnen Filterfelder und den User-Input, basierend auf dem queryset
    personen = myFilter.qs #die Einstellungen der Filter werden weitergegeben an personen im Template, s. URL


    for person in personen:
        person.jahr = person.position_held_startdate[:4]    #die einzelnen Jahre werden aus den ersten 4 Ziffern extrahiert
        #position_held_start_EU - Datum im Format TT.MM.JJJJ vorher JJJJ.MM.TT
        #Die Ziffern 8-10 (Tag) werden zusammengehängt mit den Ziffern 5-7 (Monat) und dem Jahr (Ziffern 0-4). Sie werden mit Punkten dazwischen verbunden
        person.position_held_start_EU = (person.position_held_startdate[8:10] + "." + person.position_held_startdate[5:7] + "." + person.position_held_startdate[:4])
        #hier geschieht das selbe wie bei person.position_held_start_EU
        person.position_held_end_EU = (person.position_held_enddate[8:10] + "." + person.position_held_enddate[5:7] + "." + person.position_held_enddate[:4])
        #das selbe wie bei person.position_held_start_EU
        person.birthdayEU = (person.birthday[8:10] + "." + person.birthday[5:7] + "." + person.birthday[:4])

        if person.deathday is not None:
            person.deathdayEU = (person.deathday[8:10] + "." + person.deathday[5:7] + "." + person.deathday[:4])
        person.save() #EU-Daten werden in der Datenbank abgespeichert

    # Zeitraumanzeige vgl. im Template: Zeitraum {{firstentry}} bis {{lastentry}}
    zeitraumanfang = []
    zeitraumende = []
    for person in personen:
        if person.jahr not in zeitraumanfang:
            zeitraumanfang.append(person.jahr) #Alle Regierungsbeginnjahre werden in einer Liste abgespeichert
        else:
            continue
        if person.position_held_enddate[:4] not in zeitraumende: #Alle Regierungsendejahre werden in einer Liste abgespeichert
              zeitraumende.append(person.position_held_enddate[:4])
        else:
            continue
    zeitraumanfang.sort()
    zeitraumende.sort()
    if len(zeitraumanfang) != 0:
        firstentry = zeitraumanfang[0] #Der erste Eintrag aus der Liste wird abgespeichert
        lastentry = zeitraumende[-1]   #Der letzte Eintrag aus der Liste wird abgespeichert
    else:
        firstentry = "-"
        lastentry = "-"


#------Datenbank-Update Funktion ab hier---------
    old = "undefined"
    new = "undefined"
    message = "undefined"

    if "update_button" in request.GET:
        try:
            update_items = update_database()
            old = update_items["old"]
            new = update_items["new"]
            message = "Datenbank-Update erfolgreich!"
        except:
            message = "Datenbank-Update leider nicht erfolgreich!"
#-------Datenbank-Update Funktion Ende-----------

    context = {
        'personen': personen,
        'myFilter': myFilter,       #django-filter wird übergeben
        'firstentry': firstentry,   #Zeitraumanzeige
        'lastentry': lastentry,     #Zeitraumanzeige
        'old': old,                 #Datenbank-Update
        'new': new,                 #Datenbank-Update
        'message': message          #Datenbank-Update
    }

    return render(request, "timeline/timeline.html", context)





def update_database ():

    with open("../staatsoberhaupt_filter_test.csv", encoding="utf-8") as csvdatei:
        reader = csv.DictReader(csvdatei, delimiter=",")

        count_new = 0
        count_old = 0

        new_data = True

        for row in reader:

            if row ["deathday"] == "":
                deathday = "None"
            else:
                deathday = row ["deathday"][:10]

            if row ["picture"] == "":
                picture = "None"
            else:
                picture = row ["picture"]

            if row ["gender"] == "":
                gender = "None"
            else:
                gender = row ["gender"]

            if row ["religionLabel"] == "":
                religion = "-"
            else:
                religion = row ["religionLabel"]

            if row ["predecessor"] == "":
                predecessor = "None"
            else:
                predecessor = row ["predecessor"]

            if row ["successor"] == "":
                successor = "None"
            else:
                successor = row ["successor"]

            line_data = row ["pm20id"] + row ["wikidata_object"] + row ["name"] + row ["birthday"][:10] + deathday + row ["position_held"] + row ["position_held_startdate"][:10] + row ["position_held_enddate"][:10] + picture + row ["country"] + gender + predecessor + successor + religion
            all_db_entries = Person.objects.all()

            for entry in all_db_entries:
                db_entry = str(entry.pm20id) + str(entry.wikidata_object) + str(entry.name) + str(entry.birthday) + str(entry.deathday) + str(entry.position_held) + str(entry.position_held_startdate) + str(entry.position_held_enddate) + str(entry.picture) + str(entry.country) + str(entry.gender) + str(entry.predecessor) + str(entry.successor) + str(entry.religion)

                if db_entry == line_data:
                    new_data = False

            if new_data == True:
                count_new += 1

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
                if row ["gender"] != "":
                    person.gender = row ["gender"]
                if row ["religionLabel"] != "":
                    person.religion = row ["religionLabel"]
                if row ["predecessor"] != "":
                    person.predecessor = row ["predecessor"]
                if row ["successor"] != "":
                    person.successor = row ["successor"]
                person.save()

            else:
                count_old += 1

    update_items= {
        "old":count_old,
        "new":count_new,
    }

    return update_items

def impressum(request):
    return render(request, 'timeline/impressum.html', {})
