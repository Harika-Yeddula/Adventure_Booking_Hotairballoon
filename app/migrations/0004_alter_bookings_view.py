# Generated by Django 4.1.7 on 2023-03-10 00:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0003_alter_bookings_no_of_persons"),
    ]

    operations = [
        migrations.AlterField(
            model_name="bookings",
            name="view",
            field=models.CharField(
                choices=[("Day_view", "Day view"), ("Night_view", "Night view")],
                max_length=10,
            ),
        ),
    ]
