import csv

from django.shortcuts import render, get_object_or_404
from . import models
# Create your views here.

#Startseite wird aufgerufen unter http://localhost:8000/timeline/show#

def test(request):
    return render(request,'timeline/template.html')





