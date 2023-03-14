# Generated by Django 4.1.7 on 2023-03-14 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookingTable',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('no_of_guests', models.IntegerField()),
                ('booking_date', models.DateField()),
            ],
        ),
    ]
