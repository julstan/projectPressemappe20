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

        choices = []
        have = []
        # iteriert durch die Personen und holt alle Werte der Dropdown-Filter s. unten
        for Person in queryset: #Person sind die Staatsoberhäupter
            all_values = getattr(Person, self.field_name) #all_values = alle Werte zu allen abgefragten Dropdown-Feldnamen : Bundespräsident, männlich, Deutschland, Evangelisch lutherische Kirchen, 2017-03-19
            if all_values in have:
                continue #Geht wieder an den Anfang der Schleife
            elif len(all_values) == 10 and "-" in all_values: #1900-03-02 hat 10-Stellen und "-", so werden nur die Datumsangaben gefiltert
                all_values = all_values[:4] #nur das Jahr "1800" soll rausgeschrieben werden als Filtermöglichkeit
                if all_values[:4] in have:  #prüfen auf Dopplungen
                    continue
            have.append(all_values) #Liste mit allen Werten nur 1x
            choices.append((all_values, all_values)) #Liste mit allen Werten doppelt [('weiblich', 'weiblich'),('männlich','männlich')]
                            #das erste all_values was an die Filter_query übergeben wird
                            #das zweite all_values was man auf der Webseite sieht als Auswahlmöglichkeiten
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
    #wird im Dropdown sortiert angezeigt, weil nach Amstsantritt sortiert -> chronologsich wie die Timeline
    position_held_enddate = DynamicChoiceFilter(label='Regierungsende', lookup_expr='lte', widget=Select(attrs={'class': 'form-control w-100'}))
    #wird nicht sortiert angezeigt

    gender = DynamicChoiceFilter(label='Geschlecht', widget=Select(attrs={'class': 'form-control w-100'}))
    religion = DynamicChoiceFilter(label='Religion', widget=Select(attrs={'class': 'form-control w-100'}))
    position_held = DynamicChoiceFilter(label='Position', widget=Select(attrs={'class': 'form-control w-100'}))


    class Meta:
        model = Person #hier steht unsere Model class Person
        fields = ['name', 'position_held', 'gender', 'country', 'religion', 'position_held_startdate', 'position_held_enddate', ] #Filter die ins Template übergeben werden
        exclude = ['pm20id', 'wikidata_object'] #Filter die nicht ins Template übergeben werden sollen






