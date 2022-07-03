# jeżeli użytkownik wybiera datę i godzinę to filtrowana jest lista recyclerów, którzy są dostępni w danym terminie
#
# Dostępni w danym terminie to znaczy, że w danym przedziale czasowym ilość zamówień przypisanych do recyclera nie przekracza capacity
#
# recycler agregate count orders po tym będziemy filtrować -> count orders w danej godzinie
#
# Potem z tej listy recyclerów możemy zrobić random albo first i przekażemy go do order objects create

from datetime import datetime

from django.core.validators import RegexValidator
from django.forms import CharField, Form, DateField, ModelForm, ModelChoiceField, DateTimeField, IntegerField, \
    MultipleChoiceField, ChoiceField, ModelMultipleChoiceField
from django.core.exceptions import ValidationError

#import pytz

from base.models import Client, Address, Recycler, Order, Availability, Zone

#utc = pytz.UTC
from trash.models import Trash


def capitalized_validator(value):
    if value[0].islower():
        raise ValidationError('Value must be capitalized.')

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

class RecyclerForm(Form):
    name = CharField(max_length=128, label="Nazwa firmy:")
    street = CharField(max_length=128, label="Adres firmy:")
    city = CharField(max_length=128, label="Miasto:")
    postal_code = CharField(max_length=128, label="Kod pocztowy:")
    nip = CharField(max_length=10, validators=[RegexValidator(r'^\d{1,10}$')], label="Numer NIP:")
    available_days = MultipleChoiceField(choices=Availability.choices, label="Dostępne dni odbiorów w godz. 8.00 - 18.00:")
    capacity = ChoiceField(choices=Recycler.CAPACITY_VALUES, label="Ilość klienta możliwa do obsłużenia w ciągu 2 godzin:")
    type = MultipleChoiceField(choices=Trash.choices, label="Rodzaje odbieranych odpadów:")
    zone = ModelChoiceField(queryset=Zone.objects.all(), label="Strefy odbioru odpadów:")

    # def clean(self):
    #     result = super().clean()
    #     if not self.errors:
    #         if result['name'][0].islower:
    #             raise ValidationError(
    #                 "Nazwa firmy musi zaczynać się z dużej litery."
    #             )
    #     return result

#FORMULARZE ORDER

class OrderModelForm(ModelForm):
    class Meta:
        model = Order
        fields = "__all__"