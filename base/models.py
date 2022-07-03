from django.db import models

from trash.models import Trash


class Zone(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return f"{self.name}"


class Address(models.Model):
    street = models.CharField(max_length=128)
    city = models.CharField(max_length=128)
    postal_code = models.PositiveSmallIntegerField(max_length=5)

    class Meta:
        verbose_name_plural = "Addresses"

    def __str__(self):
        return f"{self.street} {self.city} {self.postal_code}"


class Client(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    email = models.CharField(max_length=128) #walidacja
    phone = models.IntegerField(max_length=9) #walidacja przedrostek
    zone = models.ForeignKey(
       Zone, on_delete=models.CASCADE, related_name="clients", blank=True, null=True
     )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Availability(models.Model):
    DAYS = [('PN', 'Poniedziałek'), ('WT', 'Wtorek'), ('ŚR', 'Środa'), ('CZ', 'Czwartek'), ('PT', 'Piątek'), ('SB', 'Sobota')]
    day = models.CharField(choices=DAYS, max_length=15)


#django.integerchoices albo textchoices
class Recycler(models.Model):
    CAPACITY_VALUES = [('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')]
    name = models.CharField(max_length=128)
    street = models.CharField(max_length=128)
    city = models.CharField(max_length=128)
    postal_code = models.PositiveSmallIntegerField(max_length=5)
    nip = models.IntegerField(max_length=10)
    available_days = models.ManyToManyField(Availability, choices=Availability.DAYS)
    capacity = models.SmallIntegerField(choices=CAPACITY_VALUES, max_length=1, default='1')
    type = models.ForeignKey(
        Trash, on_delete=models.CASCADE, related_name="recyclers", blank=True, null=True
    )
    zone = models.ForeignKey(
        Zone, on_delete=models.CASCADE, related_name="recyclers", blank=True, null=True
    )
    def __str__(self):
        return f"{self.name} "


TIME_INTERVALS = [('ZERO', 'Wybierz godzinę odbioru'),
                  ('ONE', '8.00 - 10.00'),
                  ('TWO', '10.00 - 12.00'),
                  ('THREE', '12.00 - 14.00'),
                  ('FOUR', '14.00 - 16.00'),
                  ('FIVE', '16.00 - 18.00')
                  ]

class Order(models.Model):
    client = models.ForeignKey(
        Client, on_delete=models.CASCADE, related_name="orders", blank=True, null=True
    )
    recycler = models.ForeignKey(
        Recycler, on_delete=models.CASCADE, related_name="orders", blank=True, null=True
    )
    order_number = models.CharField(max_length=128)  # jakas walidacja ze bedzie automatycznie nadawać?
    order_day = models.ForeignKey(
        Availability, choices=Availability.DAYS, on_delete=models.CASCADE, related_name="orders", blank=True, null=True
    )
    order_time = models.CharField(choices=TIME_INTERVALS, default='ZERO', max_length=128)
    order_date = models.DateTimeField(auto_now_add=True)
    trash_type = models.ForeignKey(
        Trash, choices=Trash.TRASHES, on_delete=models.CASCADE, related_name="orders", blank=True, null=True
    )

    def __str__(self):
        return f"{self.order_number}"