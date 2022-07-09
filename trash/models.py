from django.db import models


class Trash(models.TextChoices):
    ELECTRICAL = 'EW', 'Electrical Waste',
    RECYCLED = 'RW', 'Recycled Waste',
    HAZARDOUS = 'HW', 'Hazardous Waste',
    LARGE = 'LSW', 'Large Size Waste'
type = models.CharField(choices=Trash.choices, max_length=32)


class Meta:
    verbose_name_plural = "Trashes"

def __str__(self):
    return f"{self.type}"



class EWaste(models.Model):
    EWASTES = [('DS','dishwasher'), ('TV','TV'), ('LP','laptop'), ('inne','inne')]
    type = models.CharField(choices=EWASTES, max_length=4)
    height = models.PositiveSmallIntegerField(max_length=5)
    width = models.PositiveSmallIntegerField(max_length=5)
    length = models.PositiveSmallIntegerField(max_length=5)
    weight = models.PositiveSmallIntegerField(max_length=5)

    def __str__(self):
        return f"{self.type}"


class RWaste(models.Model):
    RWASTES = [('paper','paper'), ('plastic','plastic'), ('glass','glass'), ('bio','bio')]
    type = models.CharField(choices=RWASTES, max_length=10)
    trash_amount = models.PositiveSmallIntegerField(max_length=5)

    def __str__(self):
        return f"{self.type}"


class HWaste(models.Model):
    HWASTES = [('pai','paint'),('oil', 'oil'),('med', 'medicine'), ('oth','other')]
    type = models.CharField(choices=HWASTES, max_length=3)
    trash_amount = models.PositiveSmallIntegerField(max_length=5)

    def __str__(self):
        return f"{self.type}"


class LSWaste(models.Model):
    LSWASTES = [('fur','furniture'), ('rub','rubble'), ('oth','other')]
    type = models.CharField(choices=LSWASTES, max_length=3)
    height = models.PositiveSmallIntegerField(max_length=5)
    width = models.PositiveSmallIntegerField(max_length=5)
    length = models.PositiveSmallIntegerField(max_length=5)
    weight = models.PositiveSmallIntegerField(max_length=5)

    def __str__(self):
        return f"{self.type}"
