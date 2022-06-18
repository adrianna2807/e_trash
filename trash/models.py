from django.db import models


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
