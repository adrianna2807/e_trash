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


class Availability(models.TextChoices):
    MONDAY = 'PN', 'Poniedziałek',
    TUESDAY = 'WT', 'Wtorek',
    WEDNESDAY = 'ŚR', 'Środa',
    THURSDAY = 'CZ', 'Czwartek',
    FRIDAY = 'PT', 'Piątek',
    SATURDAY = 'SB', 'Sobota'
day = models.CharField(max_length=15, choices=Availability.choices)


class Recycler(models.Model):
    CAPACITY_VALUES = [('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')]
    name = models.CharField(max_length=128)
    street = models.CharField(max_length=128)
    city = models.CharField(max_length=128)
    postal_code = models.PositiveSmallIntegerField(max_length=5)
    nip = models.IntegerField(max_length=10)
    available_days = models.CharField(choices=Availability.choices, default='PN', max_length=15)
    capacity = models.SmallIntegerField(choices=CAPACITY_VALUES, max_length=1, default='1')
    type = models.CharField(choices=Trash.choices, max_length=32)
    zone = models.ForeignKey(
        Zone, on_delete=models.CASCADE, related_name="recyclers", blank=True, null=True
    )
    def __str__(self):
        return f"{self.name} "

class TimeInterval(models.IntegerChoices):
    INTERVAL_0 = 0, 'Wybierz godzinę odbioru',
    INTERVAL_1 = 1, '8.00 - 10.00',
    INTERVAL_2 = 2, '10.00 - 12.00',
    INTERVAL_3 = 3, '12.00 - 14.00',
    INTERVAL_4 = 4, '14.00 - 16.00',
    INTERVAL_5 = 5, '16.00 - 18.00'

hour = models.CharField(choices=TimeInterval.choices, max_length=32)


class Order(models.Model):
    id = models.AutoField(primary_key=True)
    client = models.ForeignKey(
        Client, on_delete=models.CASCADE, related_name="orders", blank=True, null=True
    )
    recycler = models.ForeignKey(
        Recycler, on_delete=models.CASCADE, related_name="orders", blank=True, null=True
    )
    order_number = models.CharField(auto_created=True, max_length=14)
    order_day = models.CharField( choices=Availability.choices, default='PN', max_length=15)
    order_time = models.CharField(choices=TimeInterval.choices, default=0, max_length=128)
    order_date = models.DateTimeField(auto_now_add=True)
    zone = models.ForeignKey(
        Zone, on_delete=models.CASCADE, related_name="orders", blank=True, null=True
    )
    address = models.ForeignKey(
        Address, on_delete=models.CASCADE, related_name="orders", blank=True, null=True
    )
    trash_type = models.CharField(choices=Trash.choices, max_length=32)

    def __str__(self):
        return f"{self.order_number}"


class RecyclerAssignedOrders(models.Model):
    recycler = models.ForeignKey(
        Recycler, on_delete=models.CASCADE, related_name="assigned_orders", blank=True, null=True
    )
    order_time = models.ManyToManyField(
        Order, related_name="assigned_orders", blank=True, null=True
    )

