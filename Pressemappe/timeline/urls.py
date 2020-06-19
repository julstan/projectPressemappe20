from django.urls import path
from . import views


app_name = 'timeline'

urlpatterns = [
    path('show', views.timeline, name='show'),
]
