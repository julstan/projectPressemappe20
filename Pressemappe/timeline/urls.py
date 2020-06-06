from django.urls import path
from . import views

#Startseite wird aufgerufen unter http://localhost:8000/timeline/show#

urlpatterns = [
    path('show', views.test, name='show')
]
