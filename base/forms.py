# jeżeli użytkownik wybiera datę i godzinę to filtrowana jest lista recyclerów, którzy są dostępni w danym terminie
#
# Dostępni w danym terminie to znaczy, że w danym przedziale czasowym ilość zamówień przypisanych do recyclera nie przekracza capacity
#
# recycler agregate count orders po tym będziemy filtrować -> count orders w danej godzinie
#
# Potem z tej listy recyclerów możemy zrobić random albo first i przekażemy go do order objects create

from datetime import datetime

from django.forms import CharField, Form, DateField, ModelForm, ModelChoiceField, DateTimeField
from django.core.exceptions import ValidationError

#import pytz

from base.models import Client, Address, Recycler, Order


#utc = pytz.UTC


#FORMULARZE CLIENT

class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = "__all__"


class AddressForm(ModelForm):
    class Meta:
        model = Address
        fields = "__all__"



#FORMULARZE RECYCLER

class RecyclerModelForm(ModelForm):
    class Meta:
        model = Recycler
        fields = "__all__"


#FORMULARZE ORDER

class OrderModelForm(ModelForm):
    class Meta:
        model = Order
        fields = "__all__"