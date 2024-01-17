# Generated by Django 5.0.1 on 2024-01-15 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='bidhistory',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('itemid', models.IntegerField()),
                ('itemname', models.CharField(max_length=100)),
                ('bid', models.IntegerField()),
                ('bidtime', models.DateTimeField()),
                ('bidder', models.CharField(max_length=100)),
            ],
        ),
    ]