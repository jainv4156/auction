# Generated by Django 5.0.1 on 2024-02-13 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onedayauction', '0007_alter_auctionitem_itemimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='auctionitem',
            name='status',
            field=models.CharField(default='NotSold', max_length=100),
        ),
    ]
