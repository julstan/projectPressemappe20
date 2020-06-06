from django.shortcuts import render, get_object_or_404
from .models import Person
# Create your views here.

#Startseite wird aufgerufen unter http://localhost:8000/timeline/show#

def test(request):
    return render(request,'timeline/template.html')



def person_detail_view(request):
    obj = Person.object.get(id=1)
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
        'object' :obj,
    }
    return render(request, "timeline/template.html", context)


