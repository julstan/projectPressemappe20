from django.urls import path
from . import views

#Startseite wird aufgerufen unter localhost:8000#
app_name = 'timeline'

urlpatterns = [
    path('', views.test, name='show')
]
