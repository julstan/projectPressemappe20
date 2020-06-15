#Filter basierend auf unserem Model

import django_filters
from .models import *
class PersonFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(label='Name')
    country = django_filters.CharFilter(label='Land')


    class Meta:
        model = Person
        fields = ['name', 'country']
        exclude = ['pm20id', 'wikidata_object']




