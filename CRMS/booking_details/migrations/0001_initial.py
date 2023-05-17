# Generated by Django 4.1.7 on 2023-05-17 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car_Booking_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Pick_up_date', models.DateField()),
                ('Drop_off_date', models.DateField()),
                ('car_name', models.CharField(max_length=122)),
                ('car_company_name', models.CharField(max_length=122)),
                ('car_rent_per_day', models.IntegerField()),
                ('Car_type', models.CharField(max_length=122)),
            ],
        ),
    ]
