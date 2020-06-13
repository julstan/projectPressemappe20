from django.urls import path
from . import views

#Startseite wird aufgerufen unter localhost:8000#
app_name = 'timeline'

urlpatterns = [
    path('show', views.timeline, name='show'),
    # path('deutschland_filter', views.deutschland_filter, name='deutschland_filter'),#
]
