# Generated by Django 4.1.2 on 2022-10-29 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HotelModel',
            fields=[
                ('hotel_id', models.AutoField(primary_key=True, serialize=False)),
                ('hotel_name', models.CharField(max_length=100)),
                ('hotel_location', models.CharField(choices=[('TN', 'TN'), ('KERALA', 'KERALA'), ('KA', 'KA')], max_length=30)),
                ('hotel_description', models.CharField(max_length=50)),
                ('hotel_type', models.CharField(choices=[('APPARTMENT', 'APPARTMENT'), ('RESORT', 'RESORT')], max_length=50)),
                ('hotel_image', models.ImageField(blank=True, null=True, upload_to='hotel_image')),
                ('hotel_rating', models.PositiveIntegerField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')])),
            ],
        ),
    ]
