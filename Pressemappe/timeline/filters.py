from django.forms.widgets import TextInput
from django.forms.widgets import Select
import django_filters
from django_filters import DateFilter, CharFilter
from .models import *


class DynamicChoiceMixin(object):    #Auswahlmöglichkeiten werden dynamisch aus dem queryset generiert

    @property
    def field(self):
        queryset = self.parent.queryset
        field = super(DynamicChoiceMixin, self).field

        choices = list() #Die Auswahlmöglichkeiten in der Dropdown-Liste
        have = list()
        # iteriert durch das queryset und holt alle Werte der jeweiligen Feldnamen
        for item in queryset:
            name = getattr(item, self.field_name) #Die Feldnamen: gender, religion, country, ...
            if name in have:
                continue
            have.append(name) #Hier alle Werte
            choices.append((name, name)) #name, name = Für die entsprechenden Feldnamen die Werte, die in der Dropdown-Liste zu sehen sind
        field.choices.choices = choices
        return field


class DynamicChoiceFilter(DynamicChoiceMixin, django_filters.ChoiceFilter):
    pass



class PersonFilter(django_filters.FilterSet):  #Filterset generiert automatisch Filter basierend auf unserem Model

    #Die Arten der Filter werden hier definiert, ob Freies Suchfeld oder Dropdown + Das Design der Suchfelder wird durch Bootstrap-Klassen angepasst
    name = CharFilter(label='Name', lookup_expr='icontains',widget=TextInput(attrs={'placeholder': 'z.B. George Washington, Thomas Jefferson', 'class': 'form-control w-100'}))
    country = DynamicChoiceFilter(label='Land', widget=Select(attrs={'class': 'form-control w-100'}))


    #Datum wird extra behandelt, deshalb kommt es unten nicht in fields
    # Freies Textfeld aber nur exaktes Datum kann gefunden werden
    # StartDatum = DateFilter(label='Regierungsbeginn', field_name="position_held_startdate", lookup_expr='gte', widget=TextInput(attrs={'placeholder': 'YYYY-MM-DD', 'class': 'form-control w-100'}))  #größer und gleich als
    # EndDatum = DateFilter(label='Regierungsende', field_name="position_held_enddate", lookup_expr='lte', widget=TextInput(attrs={'placeholder': 'YYYY-MM-DD', 'class': 'form-control w-100'}))  #kleiner und gleich als

    #Dropdown-Liste mit allen Datumsfomaten
    position_held_startdate = DynamicChoiceFilter(label='Regierungsbeginn', lookup_expr='gte', widget=Select(attrs={'class': 'form-control w-100'}))
    position_held_enddate = DynamicChoiceFilter(label='Regierungsende', lookup_expr='lte', widget=Select(attrs={'class': 'form-control w-100'}))

    
    gender = DynamicChoiceFilter(label='Geschlecht', widget=Select(attrs={'class': 'form-control w-100'}))
    religion = DynamicChoiceFilter(label='Religion', widget=Select(attrs={'class': 'form-control w-100'}))
    position_held = DynamicChoiceFilter(label='Position', widget=Select(attrs={'class': 'form-control w-100'}))


    class Meta:
        model = Person #hier steht unsere Model class Person
        fields = ['name', 'position_held', 'gender', 'country', 'religion', 'position_held_startdate','position_held_enddate' ] #Filter die ins Template übergeben werden
        exclude = ['pm20id', 'wikidata_object'] #Filter die nicht ins Template übergeben werden sollen






