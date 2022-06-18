from django.db import models


class Trash(models.Model):
    TRASH = [('EW', 'Electrical Waste'), ('RW', 'Recycled Waste'), ('HW','Hazardous Waste'), ('LSW','Large Size Waste')]
    type = models.CharField(choices=TRASH, max_length=3)

    def __str__(self):
        return f"{self.type}"


class EWaste(models.Model):
    TRASH = [('DS','dishwasher'), ('TV','TV'), ('LP','laptop'), ('inne','inne')]
    type = models.CharField(choices=TRASH, max_length=4)
    height = models.PositiveSmallIntegerField(max_length=5)
    width = models.PositiveSmallIntegerField(max_length=5)
    length = models.PositiveSmallIntegerField(max_length=5)
    weight = models.PositiveSmallIntegerField(max_length=5)

    def __str__(self):
        return f"{self.type}"


class RWaste(models.Model):
    TRASH = [('paper','paper'), ('plastic','plastic'), ('glass','glass'), ('bio','bio')]
    type = models.CharField(choices=TRASH, max_length=10)
    trash_amount = models.PositiveSmallIntegerField(max_length=5)

    def __str__(self):
        return f"{self.type}"


class HWaste(models.Model):
    TRASH = [('pai','paint'),('oil', 'oil'),('med', 'medicine'), ('oth','other')]
    type = models.CharField(choices=TRASH, max_length=3)
    trash_amount = models.PositiveSmallIntegerField(max_length=5)

    def __str__(self):
        return f"{self.type}"


class LSWaste(models.Model):
    TRASH = [('fur','furniture'), ('rub','rubble'), ('oth','other')]
    type = models.CharField(choices=TRASH, max_length=3)
    height = models.PositiveSmallIntegerField(max_length=5)
    width = models.PositiveSmallIntegerField(max_length=5)
    length = models.PositiveSmallIntegerField(max_length=5)
    weight = models.PositiveSmallIntegerField(max_length=5)

    def __str__(self):
        return f"{self.type}"
