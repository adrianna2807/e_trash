from django.db import models


class Zone(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return f"{self.name}"


class Client(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    address = models.CharField(max_length=128)
    email = models.CharField(max_length=128) #walidacja
    phone = models.IntegerField(max_length=9) #walidacja przedrostek
    zone = models.ForeignKey(
        Zone, on_delete=models.CASCADE, related_name="clients", blank=True, null=True
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Address(models.Model):
    street = models.CharField(max_length=128)
    city = models.CharField(max_length=128)
    postal_code = models.PositiveSmallIntegerField(max_length=5)

    def __str__(self):
        return f"{self.street} {self.city} {self.postal_code}"


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
    order_number = models.AutoField()  # jakas walidacja ze bedzie automatycznie nadawać?
    date = models.DateField(choices=Schedule)
    order_date = models.DateTimeField(auto_now_add=True)
    trash_type = models.ForeignKey(
        Trash, on_delete=models.CASCADE, related_name="orders", blank=True, null=True
    )

    def __str__(self):
        return f"{self.order_number}"


class Trash(models.Model):
    TRASH = ['Electrical Waste', 'Recycled Waste', 'Hazardous Waste', 'Large Size Waste']
    type = models.CharField(choices=TRASH, max_length=128)

    def __str__(self):
        return f"{self.type}"


class EWaste(models.Model):
    TRASH = ['dishwasher', 'TV', 'laptop', 'inne']
    type = models.CharField(choices=TRASH, max_length=128)
    height = models.PositiveSmallIntegerField(max_length=5)
    width = models.PositiveSmallIntegerField(max_length=5)
    length = models.PositiveSmallIntegerField(max_length=5)
    weight = models.PositiveSmallIntegerField(max_length=5)

    def __str__(self):
        return f"{self.type}"


class RWaste(models.Model):
    TRASH = ['paper', 'plastic', 'glass', 'bio']
    type = models.CharField(choices=TRASH, max_length=128)
    trash_amount = models.PositiveSmallIntegerField(max_length=5)

    def __str__(self):
        return f"{self.type}"


class HWaste(models.Model):
    TRASH = ['paint', 'oil', 'medicine', 'other']
    type = models.CharField(choices=TRASH, max_length=128)
    trash_amount = models.PositiveSmallIntegerField(max_length=5)

    def __str__(self):
        return f"{self.type}"


class LSWaste(models.Model):
    TRASH = ['furniture', 'rubble', 'other']
    type = models.CharField(choices=TRASH, max_length=128)
    height = models.PositiveSmallIntegerField(max_length=5)
    width = models.PositiveSmallIntegerField(max_length=5)
    length = models.PositiveSmallIntegerField(max_length=5)
    weight = models.PositiveSmallIntegerField(max_length=5)

    def __str__(self):
        return f"{self.type}"
