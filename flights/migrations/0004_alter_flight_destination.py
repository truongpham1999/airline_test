# Generated by Django 4.2.7 on 2023-11-06 08:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("flights", "0003_passenger"),
    ]

    operations = [
        migrations.AlterField(
            model_name="flight",
            name="destination",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="arrivals",
                to="flights.airport",
            ),
        ),
    ]
