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
    address = models.ForeignKey(
        Address, on_delete=models.CASCADE, related_name="clients", blank=True, null=True
    )
    email = models.CharField(max_length=128) #walidacja
    phone = models.IntegerField(max_length=9) #walidacja przedrostek
    zone = models.ForeignKey(
       Zone, on_delete=models.CASCADE, related_name="clients", blank=True, null=True
     )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Recycler(models.Model):
    name = models.CharField(max_length=128)
    street = models.CharField(max_length=128)
    city = models.CharField(max_length=128)
    postal_code = models.PositiveSmallIntegerField(max_length=5)
    nip = models.IntegerField(max_length=10)
    type = models.ForeignKey(
        Trash, on_delete=models.CASCADE, related_name="recyclers", blank=True, null=True
    )
    zone = models.ForeignKey(
        Zone, on_delete=models.CASCADE, related_name="recyclers", blank=True, null=True
    )
    def __str__(self):
        return f"{self.name} "


class Schedule(models.Model):
    pass


class Order(models.Model):
    order_number = models.CharField(max_length=128)  # jakas walidacja ze bedzie automatycznie nadawać?
    date = models.DateField()
    order_date = models.DateTimeField(auto_now_add=True)
    trash_type = models.ForeignKey(
        Trash, on_delete=models.CASCADE, related_name="orders", blank=True, null=True
    )

    def __str__(self):
        return f"{self.order_number}"