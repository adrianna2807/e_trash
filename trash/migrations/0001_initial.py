# Generated by Django 4.0.4 on 2022-06-18 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EWaste',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('DS', 'dishwasher'), ('TV', 'TV'), ('LP', 'laptop'), ('inne', 'inne')], max_length=4)),
                ('height', models.PositiveSmallIntegerField(max_length=5)),
                ('width', models.PositiveSmallIntegerField(max_length=5)),
                ('length', models.PositiveSmallIntegerField(max_length=5)),
                ('weight', models.PositiveSmallIntegerField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='HWaste',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('pai', 'paint'), ('oil', 'oil'), ('med', 'medicine'), ('oth', 'other')], max_length=3)),
                ('trash_amount', models.PositiveSmallIntegerField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='LSWaste',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('fur', 'furniture'), ('rub', 'rubble'), ('oth', 'other')], max_length=3)),
                ('height', models.PositiveSmallIntegerField(max_length=5)),
                ('width', models.PositiveSmallIntegerField(max_length=5)),
                ('length', models.PositiveSmallIntegerField(max_length=5)),
                ('weight', models.PositiveSmallIntegerField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='RWaste',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('paper', 'paper'), ('plastic', 'plastic'), ('glass', 'glass'), ('bio', 'bio')], max_length=10)),
                ('trash_amount', models.PositiveSmallIntegerField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Trash',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('EW', 'Electrical Waste'), ('RW', 'Recycled Waste'), ('HW', 'Hazardous Waste'), ('LSW', 'Large Size Waste')], max_length=3)),
            ],
        ),
    ]