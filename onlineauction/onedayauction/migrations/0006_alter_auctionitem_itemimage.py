# Generated by Django 5.0.1 on 2024-02-05 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onedayauction', '0005_auctionitem_itemimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auctionitem',
            name='itemimage',
            field=models.ImageField(default='static/images/sitar.jpg', upload_to='static/images/'),
        ),
    ]