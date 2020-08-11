from django.forms.widgets import TextInput
from django.forms.widgets import Select
import django_filters
from django_filters import CharFilter, ChoiceFilter
from .models import *



class DynamicChoiceMixin(object):    #Auswahlmöglichkeiten werden dynamisch aus dem queryset generiert

    @property #wichtig, damit man die class DynamicChoiceMixin mit den Eigenschaften global aufrufen kann
    def field(self): # es wird definiert was ein Feld ist vgl. in fields =
        queryset = self.parent.queryset
        field = super(DynamicChoiceMixin, self).field

        choices = []
        have = []
        # iteriert durch die Personen und holt alle Werte der fields
        for Person in queryset: #Person sind die Staatsoberhäupter
            all_values = getattr(Person, self.field_name) #all_values = alle Werte zu allen abgefragten Dropdown-Feldnamen : Bundespräsident, männlich, Deutschland, Evangelisch lutherische Kirchen, 2017-03-19
            if all_values in have: #prüfen auf Dopplungen
                continue
            elif len(all_values) == 10 and "-" in all_values: #1900-03-02 hat 10-Stellen und "-", so werden nur die Datumsangaben gefiltert
                all_values = all_values[:4] #nur das Jahr "1800" soll rausgeschrieben werden als Filtermöglichkeit
                if all_values[:4] in have:  #prüfen auf Dopplungen bei den Jahren
                    continue
            have.append(all_values) #Liste mit allen Werten nur 1x - es wird auf Dopplungen überprüft und leere Werte werden nicht in die Liste mitaufgenommen
            choices.append((all_values, all_values)) #Liste mit allen Werten doppelt [('weiblich', 'weiblich'),('männlich','männlich')]
                            #das erste all_values was an die Filter_query übergeben wird s. URL

                            #das zweite all_values was man auf der Webseite sieht als Auswahlmöglichkeiten
        field.choices.choices = choices #dem richtigen Feld, werden die richtigen Auswahlmöglichkeiten zugeordnet
        return field #ChoiceField für die fünf Dropdowns die wir benutzen




class DynamicChoiceFilter(DynamicChoiceMixin, ChoiceFilter):
    pass



class PersonFilter(django_filters.FilterSet):  #Filterset generiert automatisch Filter basierend auf unserem Model

    #Die Arten der Filter werden hier definiert, ob Freies Suchfeld oder Dropdown + Das Design der Suchfelder wird durch Bootstrap-Klassen angepasst
    name = CharFilter(label='Name', lookup_expr='icontains',widget=TextInput(attrs={'placeholder': 'z.B. George Washington, Thomas Jefferson', 'class': 'form-control w-100'}))
    country = DynamicChoiceFilter(label='Land', widget=Select(attrs={'class': 'form-control w-100'}))


    # Datum hier wird extra behandelt, deshalb kommt es unten nicht in fields, sondern es muss hier das field_name in der Definition übergeben werden
    # Freies Textfeld
    # StartDatum = DateFilter(label='Regierungsbeginn', field_name="position_held_startdate", lookup_expr='gte', widget=TextInput(attrs={'placeholder': 'YYYY-MM-DD', 'class': 'form-control w-100'}))  #größer und gleich als
    # EndDatum = DateFilter(label='Regierungsende', field_name="position_held_enddate", lookup_expr='lte', widget=TextInput(attrs={'placeholder': 'YYYY-MM-DD', 'class': 'form-control w-100'}))  #kleiner und gleich als

    #Dropdown-Liste mit allen Datumsfomaten
    position_held_startdate = DynamicChoiceFilter(label='Regierungsbeginn', lookup_expr='gte', widget=Select(attrs={'class': 'form-control w-100'}))
    #wird im Dropdown sortiert angezeigt, weil nach Amstsantritt sortiert -> chronologsich wie die Timeline
    #position_held_enddate = DynamicChoiceFilter(label='Regierungsende', lookup_expr='lte', widget=Select(attrs={'class': 'form-control w-100'}))
    #wird nicht sortiert angezeigt

    gender = DynamicChoiceFilter(label='Geschlecht', widget=Select(attrs={'class': 'form-control w-100'}))
    religion = DynamicChoiceFilter(label='Religion', widget=Select(attrs={'class': 'form-control w-100'}))
    position_held = DynamicChoiceFilter(label='Position', widget=Select(attrs={'class': 'form-control w-100'}))


    class Meta:
        model = Person #hier steht unsere Model class Person
        fields = ['name', 'position_held', 'gender', 'country', 'religion', 'position_held_startdate'] #Filter die ins Template übergeben werden
        exclude = ['pm20id', 'wikidata_object', ] #Filter die nicht ins Template übergeben werden sollen






