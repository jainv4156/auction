# Generated by Django 5.0.1 on 2024-02-05 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auction24', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auctionobjects',
            name='objectid',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
