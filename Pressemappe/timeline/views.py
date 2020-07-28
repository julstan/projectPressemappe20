from django.shortcuts import render, redirect
from . import models
from .models import Person
import csv
from .filters import PersonFilter #django-filter





def timeline(request):
    personen = models.Person.objects.order_by('position_held_startdate')    #Alle Personendatensätze werden nach Startdatum der Position sortiert - Julika
    myFilter = PersonFilter(request.GET, queryset=personen)
    personen = myFilter.qs   #django-filter wird übergeben


    for person in personen:
        person.jahr = person.position_held_startdate[:4]
        person.position_held_start_EU = (person.position_held_startdate[8:10] + "." + person.position_held_startdate[5:7] + "." + person.position_held_startdate[:4])
        person.position_held_end_EU = (person.position_held_enddate[8:10] + "." + person.position_held_enddate[5:7] + "." + person.position_held_enddate[:4])
        person.birthdayEU = (person.birthday[8:10] + "." + person.birthday[5:7] + "." + person.birthday[:4])
        if person.deathday is not None:
            person.deathdayEU = (person.deathday[8:10] + "." + person.deathday[5:7] + "." + person.deathday[:4])
    zeitraumanfang = []
    zeitraumende = []
    for person in personen:
        if person.jahr not in zeitraumanfang:
            zeitraumanfang.append(person.jahr)
        else:
            continue
        if person.position_held_enddate[:4] not in zeitraumende:
              zeitraumende.append(person.position_held_enddate[:4])
        else:
            continue
    zeitraumanfang.sort()
    zeitraumende.sort()
    if len(zeitraumanfang) != 0:
        firstentry = zeitraumanfang[0]
        lastentry = zeitraumende[-1]
    else:
        firstentry = None
        lastentry = None

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


    context = {
        'personen': personen,
        'myFilter': myFilter,       #django-filter wird übergeben
        'firstentry': firstentry,
        'lastentry': lastentry,
        'old': old,
        'new': new,
        'message': message
    }

    return render(request, "timeline/timeline_neu.html", context)





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
