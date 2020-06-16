#Filter basierend auf unserem Model
from django.forms.widgets import TextInput
import django_filters
from django_filters import DateFilter, CharFilter
from .models import *


class PersonFilter(django_filters.FilterSet):
    name = CharFilter(label='Name', lookup_expr='icontains',widget=TextInput(attrs={'placeholder': 'z.B. John F. Kennedy,...'}))
    country = CharFilter(label='Land', lookup_expr='icontains',widget=TextInput(attrs={'placeholder': 'z.B. China'}))
    StartDatum = DateFilter(label='Regierungsbeginn', field_name="position_held_startdate", lookup_expr='gte', widget=TextInput(attrs={'placeholder': 'z.B. 1789-04-30'}))  #größer und gleich als
    EndDatum = DateFilter(label='Regierungsende', field_name="position_held_enddate", lookup_expr='lte',widget=TextInput(attrs={'placeholder': 'z.B. 2011-11-16'}))  #kleiner und gleich als


    class Meta:
        model = Person
        fields = ['name', 'country']
        exclude = ['pm20id', 'wikidata_object']




