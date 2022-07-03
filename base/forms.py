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

from base.models import Client, Address

#utc = pytz.UTC


#FORMULARZE CLIENT

class ClientModelForm(ModelForm):
    class Meta:
        model = Client
        fields = "__all__"


class AddressModelForm(ModelForm):
    class Meta:
        model = Address
        fields = "__all__"



#FORMULARZE RECYCLER

# def small_first_validator(value):
#     if value[0].isupper():
#         raise ValidationError('Value must be wrote with small letters.')
#
# class PollModelForm(ModelForm):
#     class Meta:
#         model = Poll
#         fields = "__all__"
#
#     def clean_poll_name(self):
#         return self.cleaned_data["name"].upper()


#FORMULARZE ORDER

# def small_validator(value):
#     if value.isupper():
#         raise ValidationError('Value must be wrote with small letters.')
#
# class AnswerModelForm(ModelForm):
#     class Meta:
#         model = Answer
#         fields = "__all__"