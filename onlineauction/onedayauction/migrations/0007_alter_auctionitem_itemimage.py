# Generated by Django 5.0.1 on 2024-02-05 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onedayauction', '0006_alter_auctionitem_itemimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auctionitem',
            name='itemimage',
            field=models.ImageField(default='images/sitar.jpg', upload_to='images/'),
        ),
    ]
